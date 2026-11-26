# Hakoot Practice — GE5072 final exam

Self-paced practice in the Hakoot look (same colours and answer shapes as
[ge5072-live-quiz](https://github.com/n-sanitdee/ge5072-live-quiz)), for the GE5072 final exam (1/2569).

- Students type a nickname and play. No host, no PIN, no timer, no leaderboard.
- After every answer: the right answer and a Thai explanation.
- One-line progress bar of small connected circles: green = right, red = wrong.
- **8 Pre-Final Sets** (the main thing): each is the whole exam in one sitting, in the exam's order and
  proportions — Section I: Unit 1 (14) · Unit 2 (14) · Unit 4 (15) · Company Profile (7); Section II:
  Describing Trends (10); Section III: External Reading (10) = 70. No question appears in two sets.
- At the end: score, score by section, the mistakes with explanations, the next Pre-Final Set, and topic
  sets for the weakest sections. An unfinished set is saved and can be continued later.
- Optional "Practice by topic": 39 sets (hand-written grammar/usage sets + one vocabulary set per lesson list).
- Nothing is sent anywhere: the name and best scores stay in the student's browser (localStorage).

## Files

| File | What |
|---|---|
| `index.html`, `style.css`, `app.js` | the page (no build step, no libraries) |
| `data.js` | GENERATED question bank — do not edit by hand |
| `tools/content.py` | hand-written sets: Units 1/2/4, Company Profile, Describing Trends, External Reading |
| `tools/vocab.csv` | the course word list (copy of Vocab-Quiz-App `vocab/GE5072_vocab.csv`) |
| `tools/build.py` | builds `data.js`: one vocabulary set per lesson word list + the 53 reading words, then deals the 8 Pre-Final Sets (`N_PREFINAL`, `QUOTA`); stamps `?v=` cache keys into `index.html` |

## Edit questions

1. Edit `tools/content.py` (right answer FIRST; the app shuffles the answers) or `tools/vocab.csv`.
2. `python3 tools/build.py`
3. Commit and push — GitHub Pages serves `main`.

The reading-word explanations quote a short snippet from the article; `build.py` reads it from the Week 15
deck builder on the teacher's Mac (OneDrive `Teaching/_slide_toolkit/build_wk15.py`). The article itself is
not in this repo.

## Content rules

All items are new: nothing copied from the coursebook exercises, homework, the Week 15 Try It items, the
Pop Quiz sets, or the final exam (never seen). Distractors that are also good English are not used.
Scope = the Thai-teacher lessons: 1.1 1.2 1.5 · 2.1 2.2 2.5 · 4.1 4.2 4.5 · Company Profile · Describing
Trends · External Reading.
