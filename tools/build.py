"""Build ../data.js for Hakoot Practice.

    python3 tools/build.py

Inputs
- tools/content.py   hand-written sets (grammar, functions, company profile, trends, reading)
- tools/vocab.csv    the GE5072 vocab list (copy of n-sanitdee/Vocab-Quiz-App vocab/GE5072_vocab.csv)
- content.ER_WORDS   the External Reading list (53 words)
- the Week 15 deck builder (OneDrive Teaching/_slide_toolkit/build_wk15.py) for the article text, so a
  reading-word explanation can quote a short snippet (≤ 12 words) of the sentence it comes from.
  The article itself is NOT copied into this public repo.

Vocabulary sets are generated: one question per word, meaning ⇄ word, three wrong answers from the
same lesson whose Thai meaning does not overlap with the right one (content.NEAR + a 4-letter check).
Seeded, so the output only changes when the inputs change.
"""
import ast
import csv
import json
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content  # noqa: E402

WK15 = os.path.expanduser('~/Library/CloudStorage/OneDrive-UniversityoftheThaiChamberofCommerce/'
                          'Teaching/_slide_toolkit/build_wk15.py')

LESSON_PART = {'1.1': 'u1', '1.2': 'u1', '1.5': 'u1', '2.1': 'u2', '2.2': 'u2', '2.5': 'u2',
               '4.1': 'u4', '4.2': 'u4', '4.5': 'u4', 'Describing': 'dt'}

# Thai filler that says nothing about meaning; removed before the overlap check.
FILLER = ['ความ', 'อย่าง', 'การ', 'ที่', 'ใน', 'ของ', 'และ', 'หรือ', 'เช่น', 'ให้', 'กับ', 'เป็น', 'มี',
          'ได้', 'ไม่', 'ใช้', 'แบบ', 'จาก', 'ต่อ', 'ทำ', 'คน']
THAI = re.compile(r'[฀-๿]')


def core(th):
    s = ''.join(THAI.findall(th))
    for f in sorted(FILLER, key=len, reverse=True):
        s = s.replace(f, '|')
    return {p[i:i + 4] for p in s.split('|') for i in range(len(p) - 3)}


def near(a, b):
    return any(a in g and b in g for g in content.NEAR)


def clash(x, y):
    return x['w'] == y['w'] or near(x['w'], y['w']) or bool(core(x['th']) & core(y['th']))


# ── the article (for snippets) ────────────────────────────────────────────
def load_article():
    """[(where, sentence with **list words**)] from build_wk15.py, or [] if the file is not here."""
    if not os.path.exists(WK15):
        return []
    tree = ast.parse(open(WK15, encoding='utf-8').read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], 'id', '') == 'ARTICLE':
            art = ast.literal_eval(node.value)
            break
    else:
        return []
    out = []
    for n, (key, _title, (head_en, _th), paras) in enumerate(art):
        if key.startswith('t'):
            out.append((f'Trend {key[1:]} heading', head_en))
        for no, sents in paras:
            for en, _th in sents:
                out.append((f'¶{no}', en))
    return out


def snippet(sentence, word, span=5, loose=False):
    """A short quote around **word** (markers removed), at most ~12 words. loose: the word may be
    marked in another form (**fostering**, **gaming the algorithm**)."""
    if loose:
        m = re.search(r'\*\*[^*]*\b' + re.escape(word) + r'[a-z]*[^*]*\*\*', sentence, re.I)
    else:
        m = re.search(r'\*\*' + re.escape(word) + r'\*\*', sentence, re.I)
    if not m:
        return None
    pre = re.sub(r'\*\*', '', sentence[:m.start()])
    post = re.sub(r'\*\*', '', sentence[m.end():])
    words = pre.split()
    left = ' '.join(words[-span:])
    if left and pre.endswith(' '):
        left += ' '
    keep = re.match(r'\S*(?:\s+\S+){0,%d}' % span, post).group(0)
    txt = left + '**' + sentence[m.start() + 2:m.end() - 2] + '**' + keep
    if len(words) > span:
        txt = '…' + txt
    if len(keep.strip()) < len(post.strip()):
        txt = txt.rstrip(',;:') + '…'
    return txt


# ── vocab items ───────────────────────────────────────────────────────────
def vocab_items(rows, pool_for, rng, kind):
    """rows: [{'w','th','ex','where'}]. One question per row, alternating the direction."""
    dirs = [k % 2 for k in range(len(rows))]
    rng.shuffle(dirs)
    items = []
    for r, d in zip(rows, dirs):
        cands = [x for x in pool_for(r) if not clash(x, r)]
        if len(cands) < 3:
            raise SystemExit(f'not enough distractors for {r["w"]}')
        wrong = rng.sample(cands, 3)
        # no two wrong answers that mean the same thing either
        for _ in range(50):
            if not any(clash(a, b) for i, a in enumerate(wrong) for b in wrong[i + 1:]):
                break
            wrong = rng.sample(cands, 3)
        if d == 0:   # word → Thai meaning
            q = f'"{r["w"]}"{r.get("where_q", "")} means …'
            opts = [r['th']] + [x['th'] for x in wrong]
        else:        # Thai meaning → word
            q = f'{r["th"]} = ?'
            opts = [r['w']] + [x['w'] for x in wrong]
        assert len(set(opts)) == 4, opts
        ex = f'**{r["w"]}**'
        if r.get('pos'):
            ex += ' (' + r['pos'].replace(' (', ', ').replace(')', '') + ')'
        ex += f' = {r["th"]}'
        if r.get('ex'):
            ex += '\n' + r['ex']
        items.append((q, opts, ex))
    return items


def chunks(seq, size=25):
    n = max(1, math.ceil(len(seq) / size))
    k, m = divmod(len(seq), n)
    out, i = [], 0
    for j in range(n):
        step = k + (1 if j < m else 0)
        out.append(seq[i:i + step])
        i += step
    return out


def build_vocab_sets():
    rng = random.Random(2569)
    sets = []
    # ── course vocab list ──
    rows = list(csv.DictReader(open(os.path.join(HERE, 'vocab.csv'), encoding='utf-8-sig')))
    lessons = []
    for r in rows:
        les = r['Lesson']
        if les not in lessons:
            lessons.append(les)
    by_lesson = {les: [{'w': r['Word'].strip(), 'th': r['Meaning'].strip(),
                        'ex': f'ตัวอย่าง: {r["Sentence"].strip()}', 'les': les}
                       for r in rows if r['Lesson'] == les] for les in lessons}
    for les in lessons:
        code = les.split()[0]
        part = LESSON_PART[code]
        label = 'Trend words' if code == 'Describing' else les
        same = by_lesson[les]
        unit = [x for l2 in lessons if LESSON_PART[l2.split()[0]] == part for x in by_lesson[l2]]

        def pool_for(r, same=same, unit=unit):
            p = [x for x in same if not clash(x, r)]
            return same if len(p) >= 6 else unit
        groups = chunks(same)
        for gi, g in enumerate(groups):
            items = vocab_items(g, pool_for, rng, 'csv')
            n = f' ({gi + 1}/{len(groups)})' if len(groups) > 1 else ''
            sets.append({'id': f'v-{code.lower().replace(".", "")[:4]}-{gi + 1}', 'part': part, 'kind': 'vocab',
                         'title': f'Words · {label}{n}', 'sub': f'{len(items)} words · meaning ⇄ word',
                         'items': items})
    # ── External Reading list ──
    art = load_article()
    er = []
    missing = []
    for w, pos, th in content.ER_WORDS:
        where, snip = None, None
        # prefer a paragraph over a heading
        for loose in (False, True):
            for loc, sent in sorted(art, key=lambda x: x[0].startswith('Trend')):
                s = snippet(sent, w, loose=loose)
                if s:
                    where, snip = loc, s
                    break
            if snip:
                break
        if art and not snip:
            missing.append(w)
        r = {'w': w, 'th': th, 'pos': pos}
        if snip:
            r['ex'] = f'{where}: “{snip}”'
            r['where_q'] = f' ({where})' if where.startswith('¶') else ''
        er.append(r)
    if missing:
        raise SystemExit(f'not found in the article: {missing}')
    groups = chunks(er, 18)
    for gi, g in enumerate(groups):
        items = vocab_items(g, lambda r: er, rng, 'er')
        sets.append({'id': f'v-er-{gi + 1}', 'part': 'er', 'kind': 'vocab',
                     'title': f'Words · External Reading ({gi + 1}/{len(groups)})',
                     'sub': f'{len(items)} words from the 53-word list', 'items': items})
    return sets, bool(art)


def check(items, sid):
    for q, a, ex in items:
        assert len(a) == 4 and len(set(a)) == 4, (sid, q)
        assert all(x.strip() for x in a), (sid, q)
        assert ex.strip(), (sid, q)


def stamp():
    """index.html loads data.js / app.js / style.css with ?v=<hash>, so phones never keep an old copy."""
    import hashlib
    idx = os.path.join(ROOT, 'index.html')
    html = open(idx, encoding='utf-8').read()
    for name in ('data.js', 'app.js', 'style.css'):
        h = hashlib.sha1(open(os.path.join(ROOT, name), 'rb').read()).hexdigest()[:8]
        html = re.sub(re.escape(name) + r'\?v=[\w]+', f'{name}?v={h}', html)
    open(idx, 'w', encoding='utf-8').write(html)


def main():
    topic = [dict(s, kind='topic') for s in content.SETS]
    vocab, had_article = build_vocab_sets()
    order = [p for p, _, _ in content.PARTS]
    all_sets = []
    for p in order:
        all_sets += [s for s in topic if s['part'] == p] + [s for s in vocab if s['part'] == p]
    ids = [s['id'] for s in all_sets]
    assert len(ids) == len(set(ids)), 'duplicate set id'
    for s in all_sets:
        check(s['items'], s['id'])
    data = {
        'parts': [{'id': p, 'en': en, 'th': th} for p, en, th in content.PARTS],
        'sets': [{'id': s['id'], 'part': s['part'], 'kind': s['kind'], 'title': s['title'], 'sub': s['sub'],
                  'qs': [{'q': q, 'a': a, 'ex': ex} for q, a, ex in s['items']]} for s in all_sets],
    }
    out = os.path.join(ROOT, 'data.js')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('// Generated by tools/build.py — edit tools/content.py or tools/vocab.csv, then rebuild.\n')
        f.write('// a[0] is the right answer; the app shuffles the answers every time.\n')
        f.write('window.HP_DATA = ')
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        f.write(';\n')
    stamp()
    nq = sum(len(s['qs']) for s in data['sets'])
    print(f'{len(data["sets"])} sets, {nq} questions → {out}')
    for p in order:
        ss = [s for s in data['sets'] if s['part'] == p]
        print(f'  {p}: {len(ss)} sets, {sum(len(s["qs"]) for s in ss)} Qs')
    if not had_article:
        print('  (build_wk15.py not found: reading-word explanations have no article snippet)')


if __name__ == '__main__':
    main()
