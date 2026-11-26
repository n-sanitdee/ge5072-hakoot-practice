# Hakoot Practice — GE5072 final exam

Self-paced practice in the Hakoot look (same colours and answer shapes as
[ge5072-live-quiz](https://github.com/n-sanitdee/ge5072-live-quiz)), for the GE5072 final exam (1/2569).
Live: https://n-sanitdee.github.io/ge5072-hakoot-practice/

- Students type a nickname and play. No host, no PIN, no timer, no leaderboard.
- **4 Pre-Final Sets × 70 questions**, each laid out like the final exam (coordinator's student notice
  `GE5072_รายละเอียดการสอบปลายภาค_1_2026`): Section I Units 1, 2, 4 (14 + 14 + 15) · Section II Company Profile (7)
  + Describing Trends (10) · Section III External Reading (10). No question appears in two sets.
- Most Section I–II questions are gaps in a short text built on the coursebook's own contexts (videos, audio
  scripts, readings, model emails and letters); the text stays on screen with the current gap highlighted and the
  gaps already answered filled in. No word ⇄ translation questions.
- After every answer: the right answer and a Thai explanation. One-line progress bar of small connected circles
  (green right / red wrong). At the end: score, score by section, the weakest section, every mistake with its
  sentence and explanation, and the next set to try. An unfinished set is saved and can be continued later.
- Nothing is sent anywhere: name, best scores and the set in progress stay in the browser (localStorage
  `hakoot-practice:v2`; a set in progress is dropped if the questions change).

## Files

| File | What |
|---|---|
| `index.html`, `style.css`, `app.js` | the page (no build step, no libraries) |
| `data.js` | GENERATED — do not edit by hand |
| `tools/prefinal.py` | Sections I–II of each set (`P()` = a text with gaps, `Q()` = a single question) + `ER_VOCAB` |
| `tools/content.py` | the reading sets used for Section III (`er-read`, `er-expr`); its other sets are no longer used |
| `tools/build.py` | builds `data.js` (checks 14/14/15/7/10/10 per set and no repeats) and stamps `?v=` cache keys |

## Edit questions

1. Edit `tools/prefinal.py` (right answer FIRST; the app shuffles the answers).
2. `python3 tools/build.py`
3. Commit and push — GitHub Pages serves `main`.

## Content rules

- Units 1, 2, 4: new texts around the book's situations, never the book's exercise texts, homework, the Week 15
  Try It items, the Pop Quiz or the final exam (never seen). Distractors that are also good English are not used.
- Company Profile and Describing Trends use only the coordinator's Supplementary Sheets
  (Team GE5072 › 01 Thai Teachers › Supplementary Sheet) and the project graph word set. "a growth" vs "growth"
  is never tested (the sheet and the Week 14 deck disagree).
