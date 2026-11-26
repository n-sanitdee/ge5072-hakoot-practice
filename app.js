// Hakoot Practice — self-paced GE5072 final-exam practice. No server: the name, best scores and the set in
// progress stay in this browser (localStorage). Questions come from data.js (tools/build.py).
//
// Pre-Final Sets = the whole exam in one sitting (Section I: Units 1, 2, 4 + Company Profile; Section II:
// Describing Trends; Section III: External Reading), 8 different sets. Topic sets = optional extra practice.
(() => {
  'use strict';

  const D = window.HP_DATA;
  const app = document.getElementById('app');
  const KEY = 'hakoot-practice:v1';
  const PARTS = D.parts;
  const PART = Object.fromEntries(PARTS.map((p) => [p.id, p]));
  const SETS = D.sets;
  const EXAMS = D.exams;
  const BY_ID = Object.fromEntries([...SETS, ...EXAMS].map((s) => [s.id, s]));
  const isExam = (id) => BY_ID[id] && BY_ID[id].kind === 'exam';
  const sizeOf = (id) => (isExam(id) ? BY_ID[id].refs.length : BY_ID[id].qs.length);

  // ── storage (per browser; never required) ─────────────────────────────
  function load() {
    try {
      return JSON.parse(localStorage.getItem(KEY)) || {};
    } catch (e) {
      return {};
    }
  }
  const store = Object.assign({name: '', best: {}, plays: {}, cur: null}, load());
  function save() {
    try {
      localStorage.setItem(KEY, JSON.stringify(store));
    } catch (e) {
      /* private mode etc.: the game still works, it just forgets */
    }
  }

  // ── helpers ───────────────────────────────────────────────────────────
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
  const fmt = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br>');
  function shuffle(a) {
    const b = a.slice();
    for (let i = b.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [b[i], b[j]] = [b[j], b[i]];
    }
    return b;
  }
  const SHAPES = [
    '<path d="M20 4 37 34H3Z" fill="#fff"/>',
    '<path d="M20 2 38 20 20 38 2 20Z" fill="#fff"/>',
    '<circle cx="20" cy="20" r="17" fill="#fff"/>',
    '<rect x="4" y="4" width="32" height="32" rx="2" fill="#fff"/>',
  ];
  const shape = (k, size) => `<svg width="${size}" height="${size}" viewBox="0 0 40 40" aria-hidden="true">${SHAPES[k]}</svg>`;
  const LOGO_COLORS = ['#e8344e', '#377ee6', '#f0b429', '#41a350'];
  function logo(size) {
    return `<span class="logo" aria-hidden="true">${SHAPES.map((p, k) =>
      `<svg width="${size}" height="${size}" viewBox="0 0 40 40">${p.replace('#fff', LOGO_COLORS[k])}</svg>`).join('')}</span>`;
  }
  function beads(n, res, cur) {
    const cls = n > 45 ? 'beads xdense' : n > 28 ? 'beads dense' : 'beads';
    let h = `<div class="${cls}" role="img" aria-label="${res.filter((r) => r === true || r === false).length} of ${n} answered">`;
    for (let i = 0; i < n; i++) {
      const c = res[i] === true ? 'ok' : res[i] === false ? 'bad' : i === cur ? 'cur' : '';
      h += `<i class="${c}"></i>`;
    }
    return h + '</div>';
  }
  const titleOf = (id) => (BY_ID[id] ? BY_ID[id].title : id);
  const scroll0 = () => window.scrollTo(0, 0);

  // ── game state ────────────────────────────────────────────────────────
  let game = null; // the set being played; also saved as store.cur so it survives closing the page

  function makeQs(list) {
    return list.map((x) => {
      const order = shuffle([0, 1, 2, 3]);
      return {q: x.q, opts: order.map((k) => ({t: x.a[k], right: k === 0})), ex: x.ex, p: x.p, tag: x.tag};
    });
  }
  function questionsOf(id) {
    const s = BY_ID[id];
    if (s.kind === 'exam') {
      return s.refs.map(([si, qi]) => {
        const src = SETS[si];
        return Object.assign({p: src.part, tag: PART[src.part].sec}, src.qs[qi]);
      });
    }
    return s.qs.map((q) => Object.assign({p: s.part}, q));
  }
  function start(id, again) {
    const list = questionsOf(id);
    // a Pre-Final Set keeps the exam's order; a topic set is reshuffled when played again
    const qs = makeQs(again && !isExam(id) ? shuffle(list) : list);
    game = {id, title: titleOf(id), qs, i: 0, res: [], pick: [], streak: 0, answered: false};
    persist();
    try {
      history.pushState({hp: 'play'}, '');
    } catch (e) {
      /* file:// in some browsers */
    }
    renderQuestion();
  }
  function persist() {
    store.cur = game && !game.finished ? game : null;
    save();
  }

  // ── screens ───────────────────────────────────────────────────────────
  function renderWelcome() {
    app.innerHTML = `
      <section class="welcome">
        ${logo(30)}
        <h1>Hakoot <span>Practice</span></h1>
        <p class="lead">GE5072 Final Exam <span class="th" lang="th">· ฝึกก่อนสอบปลายภาค</span></p>
        <form class="join" novalidate>
          <label for="nm">Your name <span class="th" lang="th">ชื่อเล่นของคุณ</span></label>
          <input id="nm" name="nm" maxlength="24" autocomplete="nickname" placeholder="Nickname" value="${esc(store.name)}" />
          <p class="err" role="alert"></p>
          <button class="btn gold" type="submit">Enter <span class="th" lang="th">เข้าเล่น</span> ▸</button>
        </form>
        <ul class="how">
          <li>📝 <span><b>${EXAMS.length} Pre-Final Sets.</b> Each covers every topic, like the final exam. <span class="th" lang="th">ทุกชุดมีครบทุกหัวข้อเหมือนข้อสอบจริง แต่ละชุดข้อไม่ซ้ำกัน</span></span></li>
          <li>⏱️ <span><b>No time limit, no competitors.</b> <span class="th" lang="th">ไม่จับเวลา ไม่มีคู่แข่ง</span></span></li>
          <li>✅ <span><b>The answer and a Thai explanation</b> right after every question. <span class="th" lang="th">เฉลยพร้อมคำอธิบายภาษาไทยทันทีทุกข้อ</span></span></li>
        </ul>
      </section>`;
    const form = app.querySelector('form');
    const input = form.querySelector('input');
    if (!store.name) input.focus();
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const v = input.value.trim().replace(/\s+/g, ' ');
      if (!v) {
        form.querySelector('.err').textContent = 'Please type your name. · กรุณาพิมพ์ชื่อ';
        input.focus();
        return;
      }
      store.name = v;
      save();
      renderHome();
    });
  }

  function badge(id) {
    const b = store.best[id];
    if (!b) return '<span class="badge">New</span>';
    const full = b.s === b.n;
    return `<span class="badge ${full ? 'full' : 'done'}">${full ? '★ ' : '✓ '}${b.s}/${b.n}</span>`;
  }
  function row(id, part, title, sub) {
    return `<button class="row" data-play="${esc(id)}"><span class="stripe p-${part}"></span>
      <span class="rt"><b>${esc(title)}</b><small>${sub}</small></span>${badge(id)}</button>`;
  }
  function examRow(s) {
    return row(s.id, 'pf', s.title, `${s.refs.length} questions · Sections I–III`);
  }

  function renderHome() {
    scroll0();
    const done = EXAMS.filter((s) => store.best[s.id]).length;
    const pct = Math.round((done / EXAMS.length) * 100);
    const cur = game && !game.finished ? game : null;
    let h = `
      <header class="top">
        <div class="brand">${logo(16)} <span>Hakoot</span> Practice</div>
        <button class="who" data-act="name" title="Change name">👤 ${esc(store.name)}</button>
      </header>
      <section class="hello">
        <h2>Hi, ${esc(store.name)}! 👋</h2>
        <p>Pick a Pre-Final Set. <span class="th" lang="th">เลือกชุดฝึกก่อนสอบได้เลย</span></p>
        <div class="overall"><span>${done} / ${EXAMS.length} Pre-Final Sets done</span><span class="meter"><b style="width:${pct}%"></b></span></div>
        ${cur ? `<div class="resume"><p>Unfinished: <b>${esc(cur.title)}</b> · question ${cur.i + 1} of ${cur.qs.length} <span class="th" lang="th">ทำต่อจากเดิมได้</span></p>
          <button class="btn gold" data-act="resume">Continue ▸</button></div>` : ''}
      </section>
      <section class="group" id="g-pf">
        <h3>Pre-Final Sets <small class="th" lang="th">ชุดฝึกก่อนสอบปลายภาค</small></h3>
        <p class="note">Each set follows the final exam: <b>Section I</b> Units 1, 2, 4 + Company Profile · <b>Section II</b> Describing Trends · <b>Section III</b> External Reading.
          <span class="th" lang="th">ทุกชุดครบทุกหัวข้อ เรียงแบบข้อสอบปลายภาค และข้อไม่ซ้ำกันข้ามชุด</span></p>
        <div class="rows">${EXAMS.map(examRow).join('')}</div>
      </section>
      <details class="more">
        <summary>Practice by topic <span class="th" lang="th">ฝึกแยกหัวข้อ (ไม่บังคับ)</span></summary>
        <nav class="chips" aria-label="Topics">
          ${PARTS.map((p) => `<a class="chip" href="#g-${p.id}"><i class="p-${p.id}"></i>${esc(p.en.split(' · ')[0])}</a>`).join('')}
        </nav>`;
    for (const p of PARTS) {
      const topic = SETS.filter((s) => s.part === p.id && s.kind === 'topic');
      const vocab = SETS.filter((s) => s.part === p.id && s.kind === 'vocab');
      h += `<section class="group" id="g-${p.id}">
        <h3>${esc(p.en)} <small class="th" lang="th">${esc(p.th)}</small></h3>
        ${topic.length ? `<div class="kind">${p.id === 'er' ? 'Reading' : 'Grammar · functions · usage'}</div>
        <div class="rows">${topic.map((s) => row(s.id, p.id, s.title, `${s.qs.length} questions · ${esc(s.sub)}`)).join('')}</div>` : ''}
        ${vocab.length ? `<div class="kind">Vocabulary · every word on the list</div>
        <div class="rows">${vocab.map((s) => row(s.id, p.id, s.title, esc(s.sub))).join('')}</div>` : ''}
      </section>`;
    }
    h += `</details>
      <p class="foot">Your name and scores stay on this phone only. <span class="th" lang="th">ชื่อและคะแนนเก็บไว้ในเครื่องนี้เท่านั้น ไม่มีการเก็บคะแนน</span><br>GE5072 · 1/2569</p>`;
    app.innerHTML = h;
    // open "Practice by topic" when a topic chip / anchor is used
    app.querySelectorAll('.chip').forEach((a) => a.addEventListener('click', () => {
      app.querySelector('details.more').open = true;
    }));
  }

  function renderQuestion() {
    const g = game;
    const q = g.qs[g.i];
    const n = g.qs.length;
    const right = g.res.filter((r) => r === true).length;
    const wrong = g.res.filter((r) => r === false).length;
    app.innerHTML = `
      <header class="qtop">
        <button class="x" data-act="quit" aria-label="Back to all sets" title="Back to all sets (your place is saved)">✕</button>
        <div class="qmeta"><b>${esc(g.title)}</b><span>Question ${g.i + 1} of ${n}</span></div>
        <div class="tally" aria-label="${right} right, ${wrong} wrong"><span class="g">✓ ${right}</span><span class="r">✗ ${wrong}</span></div>
      </header>
      ${beads(n, g.res, g.i)}
      <section class="qcard">
        ${q.tag ? `<span class="tag">${esc(q.tag)}</span>` : ''}
        <p class="qtext">${fmt(q.q)}</p>
      </section>
      <div class="tiles" role="group" aria-label="Answers">
        ${q.opts.map((o, k) => `<button class="tile t${k}" data-k="${k}" aria-label="Answer ${k + 1}: ${esc(o.t)}">${shape(k, 26)}<span>${esc(o.t)}</span></button>`).join('')}
      </div>
      <div id="fb"></div>`;
    g.answered = false;
    scroll0();
  }

  function answer(k, replay) {
    const g = game;
    if (!g || g.answered) return;
    g.answered = true;
    const q = g.qs[g.i];
    const ok = q.opts[k].right;
    if (!replay) {
      g.res[g.i] = ok;
      g.pick[g.i] = k;
      g.streak = ok ? g.streak + 1 : 0;
      persist();
    }
    const tiles = app.querySelector('.tiles');
    tiles.classList.add('done');
    tiles.querySelectorAll('.tile').forEach((b, j) => {
      b.disabled = true;
      if (q.opts[j].right) {
        b.classList.add('right');
        b.insertAdjacentHTML('beforeend', '<span class="mark" aria-hidden="true">✓</span>');
      } else if (j === k) {
        b.classList.add('chosen', 'wrong');
        b.insertAdjacentHTML('beforeend', '<span class="mark" aria-hidden="true">✗</span>');
      }
    });
    const bead = app.querySelectorAll('.beads i')[g.i];
    bead.classList.remove('cur');
    bead.classList.add(ok ? 'ok' : 'bad');
    const right = g.res.filter((r) => r === true).length;
    const wrong = g.res.filter((r) => r === false).length;
    app.querySelector('.tally').innerHTML = `<span class="g">✓ ${right}</span><span class="r">✗ ${wrong}</span>`;
    const last = g.i === g.qs.length - 1;
    const rightText = q.opts.find((o) => o.right).t;
    const fb = document.getElementById('fb');
    fb.innerHTML = `
      <section class="fb ${ok ? 'good' : 'bad'}" role="status">
        <div class="fb-head">${ok ? '✓ Correct!' : '✗ Not quite'} <span class="th" lang="th">${ok ? 'ถูกต้อง' : 'ยังไม่ถูก'}</span>
          ${ok && g.streak >= 3 ? `<span class="streak">🔥 ${g.streak} in a row</span>` : ''}</div>
        <div class="fb-body">
          ${ok ? '' : `<p class="fb-ans">Answer · <span class="th" lang="th">เฉลย</span>: <b>${esc(rightText)}</b></p>`}
          <p class="fb-ex" lang="th"><span class="lbl">คำอธิบาย · WHY</span>${fmt(q.ex)}</p>
          <button class="btn gold" data-act="next">${last ? 'See my score <span class="th" lang="th">ดูคะแนน</span> ▸' : 'Next question <span class="th" lang="th">ข้อต่อไป</span> ▸'}</button>
        </div>
      </section>`;
    const box = fb.firstElementChild;
    const btn = box.querySelector('[data-act="next"]');
    requestAnimationFrame(() => {
      const r = box.getBoundingClientRect();
      if (r.bottom > window.innerHeight) box.scrollIntoView({behavior: 'smooth', block: 'end'});
      btn.focus({preventScroll: true});
    });
  }

  function next() {
    const g = game;
    if (!g || !g.answered) return;
    if (g.i < g.qs.length - 1) {
      g.i++;
      persist();
      renderQuestion();
    } else {
      finish();
    }
  }

  function finish() {
    const g = game;
    g.finished = true;
    const n = g.qs.length;
    const s = g.res.filter((r) => r === true).length;
    const prev = store.best[g.id];
    const isBest = !prev || s / n > prev.s / prev.n;
    if (isBest) store.best[g.id] = {s, n};
    store.plays[g.id] = (store.plays[g.id] || 0) + 1;
    persist();
    renderEnd(g, s, n, prev, isBest);
  }

  function message(p) {
    if (p === 1) return ['🏆', 'Perfect score!', 'เต็ม! สุดยอดมาก'];
    if (p >= 0.8) return ['🎉', 'Excellent!', 'เก่งมาก พร้อมสอบแล้ว'];
    if (p >= 0.6) return ['👏', 'Good job!', 'ดีมาก อ่านคำอธิบายข้อที่ผิดอีกนิด'];
    if (p >= 0.4) return ['💪', 'Nice try!', 'ทวนข้อที่ผิด แล้วลองชุดถัดไปนะ'];
    return ['📚', 'Keep practising!', 'ค่อย ๆ ทวนทีละข้อ แล้วลองชุดถัดไปอีกรอบ'];
  }

  // score per part (Section I units, Company Profile, Section II, Section III)
  function breakdown(g) {
    const t = {};
    g.qs.forEach((q, i) => {
      t[q.p] = t[q.p] || {s: 0, n: 0};
      t[q.p].n++;
      if (g.res[i] === true) t[q.p].s++;
    });
    return PARTS.filter((p) => t[p.id]).map((p) => Object.assign({p}, t[p.id]));
  }

  // The next set to try: the next unplayed Pre-Final Set (then the lowest-scoring one);
  // plus, after a Pre-Final Set, topic sets for the two weakest parts.
  function suggestions(g) {
    const out = [];
    const add = (id) => {
      if (id && id !== g.id && !out.includes(id)) out.push(id);
    };
    const k = EXAMS.findIndex((e) => e.id === g.id);
    const ring = EXAMS.slice(k + 1).concat(EXAMS.slice(0, Math.max(k, 0)));
    add((ring.find((e) => !store.best[e.id]) || ring.slice().sort((a, b) =>
      store.best[a.id].s / store.best[a.id].n - store.best[b.id].s / store.best[b.id].n)[0] || {}).id);
    const weak = breakdown(g).filter((b) => b.s < b.n).sort((a, b) => a.s / a.n - b.s / b.n).slice(0, 2);
    for (const b of weak) {
      const pool = SETS.filter((s) => s.part === b.p.id && s.kind === 'topic');
      add((pool.find((s) => !store.best[s.id]) || pool[0] || {}).id);
    }
    return out;
  }
  function partOf(id) {
    return isExam(id) ? 'pf' : BY_ID[id].part;
  }
  function subOf(id) {
    const s = BY_ID[id];
    if (s.kind === 'exam') return `${s.refs.length} questions · Sections I–III`;
    return `${PART[s.part].en} · ${s.qs.length} questions`;
  }

  function renderEnd(g, s, n, prev, isBest) {
    scroll0();
    const p = s / n;
    const [emoji, en, th] = message(p);
    const sug = suggestions(g);
    const misses = g.qs.map((q, i) => ({q, i})).filter((x) => g.res[x.i] === false);
    const bd = isExam(g.id) ? breakdown(g) : [];
    let best = '';
    if (prev && isBest) best = `<p class="bestline new">⭐ New best! (before: ${prev.s}/${prev.n})</p>`;
    else if (prev) best = `<p class="bestline">Your best: ${prev.s}/${prev.n}</p>`;
    const first = sug[0];
    app.innerHTML = `
      <section class="end">
        <div class="trophy" aria-hidden="true">${emoji}</div>
        <h2>${esc(en)} Well done, ${esc(store.name)}!</h2>
        <p class="setname">${esc(g.title)}</p>
        <div class="bigscore" aria-label="${s} out of ${n}">${s}<span>/${n}</span></div>
        <p class="pct">${Math.round(p * 100)}% correct <span class="th" lang="th">${esc(th)}</span></p>
        ${beads(n, g.res, -1)}
        ${best}
        ${bd.length ? `<table class="secs"><caption>Score by section <span class="th" lang="th">คะแนนแยกตามส่วน</span></caption>
          ${bd.map((b) => `<tr><th scope="row"><i class="p-${b.p.id}"></i>${esc(b.p.sec)}</th><td>${b.s}/${b.n}</td>
            <td class="bar"><span><b style="width:${Math.round((b.s / b.n) * 100)}%"></b></span></td></tr>`).join('')}
          </table>` : ''}
        <div class="actions">
          ${first ? `<button class="btn gold next-set" data-play="${esc(first)}"><span>Try another set <span class="th" lang="th">ลองชุดถัดไป</span> ▸</span><small>${esc(titleOf(first))}</small></button>` : ''}
          <div class="split">
            <button class="btn ghost" data-act="again">↻ Play again</button>
            <button class="btn ghost" data-act="home">All sets</button>
          </div>
        </div>
        ${sug.length > 1 ? `<section class="box"><h3>Practise your weak spots <small class="th" lang="th">ฝึกเพิ่มเฉพาะส่วนที่ยังพลาด</small></h3>
          <div class="rows">${sug.slice(1).map((id) => row(id, partOf(id), titleOf(id), esc(subOf(id)))).join('')}</div></section>` : ''}
        <section class="box">
          <h3>${misses.length ? `Check your mistakes <small class="th" lang="th">ทบทวนข้อที่ตอบผิด (${misses.length})</small>` : 'Mistakes'}</h3>
          ${misses.length ? `<ul class="mist">${misses.map(({q, i}) => `<li>
              ${q.tag ? `<span class="mtag">${esc(q.tag)}</span>` : ''}
              <span class="mq">${i + 1}. ${fmt(q.q)}</span>
              <span class="mine">✗ ${esc(q.opts[g.pick[i]].t)}</span>
              <span class="ok">✓ ${esc(q.opts.find((o) => o.right).t)}</span>
              <p class="fb-ex" lang="th">${fmt(q.ex)}</p></li>`).join('')}</ul>`
            : '<p class="allright">None — every answer was right! <span class="th" lang="th">ถูกทุกข้อ เยี่ยมมาก</span></p>'}
        </section>
      </section>`;
  }

  function resume() {
    if (!game) return;
    const answered = game.res[game.i] === true || game.res[game.i] === false;
    renderQuestion();
    if (answered) answer(game.pick[game.i], true); // show the same answer + explanation again
  }

  // ── events ────────────────────────────────────────────────────────────
  app.addEventListener('click', (e) => {
    const t = e.target.closest('[data-k],[data-act],[data-play]');
    if (!t) return;
    if (t.dataset.k !== undefined) return answer(Number(t.dataset.k));
    if (t.dataset.play) {
      if (game && !game.finished && game.id !== t.dataset.play && game.res.length &&
          !window.confirm(`Start a new set? Your unfinished "${game.title}" will be lost.\nเริ่มชุดใหม่ไหม ชุดที่ทำค้างไว้จะหายไป`)) return;
      return start(t.dataset.play, false);
    }
    switch (t.dataset.act) {
      case 'next': return next();
      case 'quit': return renderHome();
      case 'resume': return resume();
      case 'again': return start(game.id, true);
      case 'home': game = null; persist(); return renderHome();
      case 'name': return renderWelcome();
    }
  });
  document.addEventListener('keydown', (e) => {
    if (!game || game.finished || e.target.closest('input') || e.metaKey || e.ctrlKey || e.altKey) return;
    if (!app.querySelector('.tiles')) return;
    const map = {1: 0, 2: 1, 3: 2, 4: 3, a: 0, b: 1, c: 2, d: 3};
    const k = map[e.key.toLowerCase()];
    if (k !== undefined && !game.answered) {
      e.preventDefault();
      answer(k);
    } else if ((e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowRight') && game.answered && !e.target.closest('button')) {
      e.preventDefault();
      next();
    }
  });
  // Phone "Back" during a set goes to the list; the set waits there under "Continue".
  window.addEventListener('popstate', () => {
    if (game && !game.finished && app.querySelector('.tiles')) renderHome();
  });

  // a set left unfinished last time (only if it still exists in this version of the questions)
  if (store.cur && BY_ID[store.cur.id] && store.cur.qs && store.cur.qs.length === sizeOf(store.cur.id)) game = store.cur;
  else store.cur = null;
  if (store.name) renderHome();
  else renderWelcome();
})();
