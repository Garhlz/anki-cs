"""校验卡片格式、知识地图引用与报告统计；不验证技术正确性。"""
from collections import Counter
import json
from pathlib import Path
import re
import sys

import yaml

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
TYPES = {'concept', 'mechanism', 'comparison', 'tradeoff', 'application', 'synthesis'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate():
    cards, ids, contents, questions = [], set(), set(), set()
    for domain in ('mysql', 'redis'):
        for path in sorted((OUT / domain).rglob('*.md')):
            raw = path.read_text(encoding='utf-8')
            match = re.fullmatch(r'---\n(.*?)\n---\n(.*)', raw, re.S)
            require(match, f'{path}: Front Matter 分隔符错误')
            meta = yaml.safe_load(match[1])
            require(isinstance(meta, dict), f'{path}: YAML 必须为映射')
            required = {'id', 'domain', 'topic', 'priority', 'type', 'tags', 'sources'}
            require(required <= meta.keys(), f'{path}: 缺少字段')
            ident = meta['id']
            require(isinstance(ident, str) and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', ident), f'{path}: ID 非法')
            require(ident not in ids and path.stem == ident, f'{path}: 重复 ID 或文件名不符')
            require(meta['domain'] == domain and ident.startswith(domain + '-'), f'{path}: domain 不符')
            require(meta['priority'] in {'P0', 'P1', 'P2'} and meta['type'] in TYPES, f'{path}: 枚举非法')
            require(isinstance(meta['topic'], str) and re.fullmatch(r'[a-z]+(?:-[a-z]+)*', meta['topic']), f'{path}: topic 非法')
            for field in ('tags', 'sources'):
                require(isinstance(meta[field], list) and meta[field] and all(isinstance(x, str) and x.strip() for x in meta[field]), f'{path}: {field} 结构非法')
            for source in meta['sources']:
                target = (ROOT / source).resolve()
                allowed = any(target.is_relative_to((ROOT / 'CS-Base' / d).resolve()) for d in ('mysql', 'redis'))
                require(allowed and target.is_file() and target.suffix == '.md', f'{path}: 来源不合法 {source}')
            body = match[2]
            require(re.findall(r'^# .*$', body, re.M) == ['# Question', '# Answer', '# Extra'], f'{path}: 标题数量或顺序错误')
            q, a, extra = re.split(r'^# (?:Question|Answer|Extra)\s*\n', body, flags=re.M)[1:]
            require(q.strip() and a.strip(), f'{path}: 空题干或答案')
            fingerprint = re.sub(r'\s+', '', q + a)
            normalized_q = re.sub(r'\s+', '', q)
            require(fingerprint not in contents and normalized_q not in questions, f'{path}: 重复题干或问答')
            contents.add(fingerprint)
            questions.add(normalized_q)
            ids.add(ident)
            cards.append(meta)
    require(cards, '没有卡片')
    rows = []
    for line in (OUT / 'knowledge-map.md').read_text().splitlines():
        if line.startswith('| mysql |') or line.startswith('| redis |'):
            cells = [s.strip() for s in line.strip('|').split('|')]
            require(len(cells) == 8, '知识地图列数错误')
            domain, topic, unit, priority, coverage, links, sources, note = cells
            require(coverage in {'uncovered', 'partial', 'covered', 'skipped'}, f'{unit}: 状态非法')
            require(priority in {'P0', 'P1', 'P2'}, f'{unit}: 优先级非法')
            mapped = re.findall(r'\[([^]]+)\]\((?:mysql|redis)/[^)]+\.md\)', links)
            require((bool(mapped) if coverage in {'covered', 'partial'} else not mapped), f'{unit}: 覆盖状态与引用不符')
            for ident in mapped:
                require(ident in ids, f'{unit}: 卡片不存在 {ident}')
                meta = next(m for m in cards if m['id'] == ident)
                require((meta['domain'], meta['topic'], meta['priority']) == (domain, topic, priority), f'{unit}: 元数据不一致')
            rows.append((unit.split('：')[0], priority, coverage, mapped))
    require(len({r[0] for r in rows}) == len(rows), '知识单元 ID 重复')
    references = [i for r in rows for i in r[3]]
    require(set(references) == ids, '存在未登记卡片或地图缺失')
    require(not any(p.stat().st_size == 0 for p in OUT.rglob('*') if p.is_file()), '存在空文件')
    summary = {
        'source_files': {d: len(list((ROOT / 'CS-Base' / d).rglob('*.md'))) for d in ('mysql', 'redis')},
        'knowledge_units': len(rows),
        'unit_priority': dict(sorted(Counter(r[1] for r in rows).items())),
        'coverage': dict(sorted(Counter(r[2] for r in rows).items())),
        'cards': len(cards),
        'domain': dict(sorted(Counter(m['domain'] for m in cards).items())),
        'topic': dict(sorted(Counter(m['domain'] + '/' + m['topic'] for m in cards).items())),
        'type': {t: sum(m['type'] == t for m in cards) for t in sorted(TYPES)},
        'card_priority': dict(sorted(Counter(m['priority'] for m in cards).items())),
    }
    report = OUT / 'review-report.md'
    if report.exists():
        block = re.search(r'<!-- stats -->\s*```json\n(.*?)\n```', report.read_text(), re.S)
        require(block and json.loads(block[1]) == summary, '报告统计与实际文件不一致，请更新报告')
    return summary


if __name__ == '__main__':
    try:
        print(json.dumps(validate(), ensure_ascii=False, indent=2))
        print('校验通过：格式、来源路径、唯一性、地图引用和已有报告统计。')
    except (ValueError, TypeError, KeyError, yaml.YAMLError) as error:
        print(f'校验失败：{error}', file=sys.stderr)
        sys.exit(1)
