// Hakoot Practice — self-paced GE5072 final-exam practice. No server: the name, best scores and
// play counts stay in this browser (localStorage). Questions come from data.js (tools/build.py).
(() => {
  'use strict';

  const D = window.HP_DATA;
  const app = document.getElementById('app');
  const KEY = 'hakoot-practice:v1';
  const PARTS = D.parts;
  const PART = Object.fromEntries(PARTS.map((p) => [p.id, p]));
  const SETS = D.sets;
  const BY_ID = Object.fromEntries(SETS.map((s) => [s.id, s]));

  // Mixed sets draw new questions from every topic each time they are played.
  const MIXES = [
    {id: 'mix-25', title: 'Mixed Practice', th: 'สุ่มข้อจากทุกหัวข้อ', n: 25,
      plan: {u1: 5, u2: 5, u4: 5, cp: 3, dt: 4, er: 3}},
    {id: 'mix-50', title: 'Big Mix', th: 'ชุดใหญ่ สุ่มจากทุกหัวข้อ', n: 50,
      plan: {u1: 10, u2: 10, u4: 11, cp: 5, dt: 7, er: 7}},
  ];
  const MIX_BY_ID = Object.fromEntries(MIXES.map((m) => [m.id, m]));

  // ── storage (per browser; never required) ─────────────────────────────
  function load() {
    try {
      return JSON.parse(localStorage.getItem(KEY)) || {};
    } catch (e) {
      return {};
    }
  }
  const store = Object.assign({name: '', best: {}, plays: {}}, load());
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
    let h = `<div class="${cls}" role="img" aria-label="${res.filter((r) => r !== undefined).length} of ${n} answered">`;
    for (let i = 0; i < n; i++) {
      const c = res[i] === true ? 'ok' : res[i] === false ? 'bad' : i === cur ? 'cur' : '';
      h += `<i class="${c}"></i>`;
    }
    return h + '</div>';
  }
  const titleOf = (id) => (BY_ID[id] ? BY_ID[id].title : MIX_BY_ID[id] ? MIX_BY_ID[id].title : id);
  const sizeOf = (id) => (BY_ID[id] ? BY_ID[id].qs.length : MIX_BY_ID[id].n);
  function scroll0() {
    window.scrollTo(0, 0);
  }

  // ── game state ────────────────────────────────────────────────────────
  let game = null; // the set being played (kept while the player looks at the list = "paused")

  function makeQs(list) {
    return list.map((x) => {
      const order = shuffle([0, 1, 2, 3]);
      return {q: x.q, opts: order.map((k) => ({t: x.a[k], right: k === 0})), ex: x.ex, tag: x.tag, part: x.part};
    });
  }
  function mixQuestions(mix) {
    const out = [];
    for (const p of PARTS) {
      const pool = [];
      for (const s of SETS) if (s.part === p.id) for (const q of s.qs) pool.push(Object.assign({tag: s.title, part: s.part}, q));
      out.push(...shuffle(pool).slice(0, mix.plan[p.id] || 0));
    }
    return shuffle(out);
  }
  function start(id, again) {
    let qs;
    let part = null;
    if (MIX_BY_ID[id]) {
      qs = makeQs(mixQuestions(MIX_BY_ID[id]));
    } else {
      const s = BY_ID[id];
      part = s.part;
      const list = s.qs.map((q) => Object.assign({part: s.part}, q));
      qs = makeQs(again ? shuffle(list) : list);
    }
    game = {id, title: titleOf(id), part, qs, i: 0, res: [], pick: [], streak: 0, answered: false};
    try {
      history.pushState({hp: 'play'}, '');
    } catch (e) {
      /* file:// in some browsers */
    }
    renderQuestion();
  }

  // ── screens ───────────────────────────────────────────────────────────
  function renderWelcome() {
    game = null;
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
          <li>⏱️ <span><b>No time limit, no competitors.</b> <span class="th" lang="th">ไม่จับเวลา ไม่มีคู่แข่ง</span></span></li>
          <li>✅ <span><b>The answer and a Thai explanation</b> right after every question. <span class="th" lang="th">เฉลยพร้อมคำอธิบายภาษาไทยทันทีทุกข้อ</span></span></li>
          <li>🔁 <span><b>${SETS.length + MIXES.length} sets.</b> Play as many as you like. <span class="th" lang="th">เล่นซ้ำได้ไม่จำกัด</span></span></li>
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

  function renderHome() {
    scroll0();
    const done = SETS.filter((s) => store.best[s.id]).length;
    const pct = Math.round((done / SETS.length) * 100);
    let h = `
      <header class="top">
        <div class="brand">${logo(16)} <span>Hakoot</span> Practice</div>
        <button class="who" data-act="name" title="Change name">👤 ${esc(store.name)}</button>
      </header>
      <section class="hello">
        <h2>Hi, ${esc(store.name)}! 👋</h2>
        <p>Pick a set to practise. <span class="th" lang="th">เลือกชุดที่อยากฝึกได้เลย</span></p>
        <div class="overall"><span>${done} / ${SETS.length} sets done</span><span class="meter"><b style="width:${pct}%"></b></span></div>
        ${game && !game.finished ? `<div class="resume"><p>Paused: <b>${esc(game.title)}</b> · question ${game.i + 1} of ${game.qs.length}</p>
          <button class="btn gold" data-act="resume">Continue ▸</button></div>` : ''}
      </section>
      <nav class="chips" aria-label="Topics">
        <a class="chip" href="#g-mix"><i class="p-mix"></i>Mixed</a>
        ${PARTS.map((p) => `<a class="chip" href="#g-${p.id}"><i class="p-${p.id}"></i>${esc(p.en.split(' · ')[0])}</a>`).join('')}
      </nav>
      <section class="group" id="g-mix">
        <h3>Mixed practice <small class="th" lang="th">สุ่มข้อจากทุกหัวข้อ · ได้ข้อใหม่ทุกครั้ง</small></h3>
        <div class="rows">
          ${MIXES.map((m) => row(m.id, 'mix', m.title, `${m.n} questions from every topic`)).join('')}
        </div>
      </section>`;
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
    h += `<p class="foot">Your name and scores stay on this phone only. <span class="th" lang="th">ชื่อและคะแนนเก็บไว้ในเครื่องนี้เท่านั้น</span><br>GE5072 · 1/2569</p>`;
    app.innerHTML = h;
  }

  function renderQuestion() {
    const g = game;
    const q = g.qs[g.i];
    const n = g.qs.length;
    const right = g.res.filter((r) => r === true).length;
    const wrong = g.res.filter((r) => r === false).length;
    app.innerHTML = `
      <header class="qtop">
        <button class="x" data-act="quit" aria-label="Back to all sets" title="Back to all sets">✕</button>
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

  function answer(k) {
    const g = game;
    if (!g || g.answered) return;
    g.answered = true;
    const q = g.qs[g.i];
    const ok = q.opts[k].right;
    g.res[g.i] = ok;
    g.pick[g.i] = k;
    g.streak = ok ? g.streak + 1 : 0;
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
    // progress + tally
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
    save();
    renderEnd(g, s, n, prev, isBest);
  }

  function message(p) {
    if (p === 1) return ['🏆', 'Perfect score!', 'เต็ม! สุดยอดมาก'];
    if (p >= 0.8) return ['🎉', 'Excellent!', 'เก่งมาก พร้อมสอบแล้ว'];
    if (p >= 0.6) return ['👏', 'Good job!', 'ดีมาก อ่านคำอธิบายข้อที่ผิดอีกนิด'];
    if (p >= 0.4) return ['💪', 'Nice try!', 'ทวนข้อที่ผิด แล้วลองอีกครั้งนะ'];
    return ['📚', 'Keep practising!', 'ค่อย ๆ ทวนทีละข้อ แล้วเล่นใหม่อีกรอบ'];
  }

  // Up to three sets to try next: unplayed first (same topic, then the weakest other topics), then low scores.
  function suggestions(g) {
    const out = [];
    const add = (id) => {
      if (id && id !== g.id && !out.includes(id) && out.length < 3) out.push(id);
    };
    const unplayed = (s) => !store.best[s.id];
    const missByPart = {};
    g.qs.forEach((q, i) => {
      if (g.res[i] === false) missByPart[q.part] = (missByPart[q.part] || 0) + 1;
    });
    if (g.part) {
      const same = SETS.filter((s) => s.part === g.part && unplayed(s) && s.id !== g.id);
      add(same.find((s) => s.kind === 'topic')?.id || same[0]?.id);
    }
    const done = (p) => SETS.filter((s) => s.part === p && store.best[s.id]).length / SETS.filter((s) => s.part === p).length;
    const order = PARTS.map((p) => p.id).filter((p) => p !== g.part)
      .sort((a, b) => (missByPart[b] || 0) - (missByPart[a] || 0) || done(a) - done(b));
    for (const p of order) {
      const s = SETS.find((x) => x.part === p && unplayed(x) && x.kind === 'topic') || SETS.find((x) => x.part === p && unplayed(x));
      if (s) add(s.id);
      if (out.length >= 2) break;
    }
    if (!MIX_BY_ID[g.id]) add('mix-25');
    else add(g.id === 'mix-25' ? 'mix-50' : 'mix-25');
    const low = SETS.filter((s) => store.best[s.id]).sort((a, b) => store.best[a.id].s / store.best[a.id].n - store.best[b.id].s / store.best[b.id].n);
    for (const s of low) add(s.id);
    return out;
  }
  function partOf(id) {
    return BY_ID[id] ? BY_ID[id].part : 'mix';
  }
  function subOf(id) {
    const s = BY_ID[id];
    if (!s) return `${MIX_BY_ID[id].n} questions from every topic`;
    return `${PART[s.part].en} · ${s.qs.length} questions`;
  }

  function renderEnd(g, s, n, prev, isBest) {
    scroll0();
    const p = s / n;
    const [emoji, en, th] = message(p);
    const sug = suggestions(g);
    const misses = g.qs.map((q, i) => ({q, i})).filter((x) => g.res[x.i] === false);
    let best = '';
    if (prev && isBest) best = `<p class="bestline new">⭐ New best! (before: ${prev.s}/${prev.n})</p>`;
    else if (prev) best = `<p class="bestline">Your best: ${prev.s}/${prev.n}</p>`;
    app.innerHTML = `
      <section class="end">
        <div class="trophy" aria-hidden="true">${emoji}</div>
        <h2>${esc(en)} Well done, ${esc(store.name)}!</h2>
        <p class="setname">${esc(g.title)}</p>
        <div class="bigscore" aria-label="${s} out of ${n}">${s}<span>/${n}</span></div>
        <p class="pct">${Math.round(p * 100)}% correct <span class="th" lang="th">${esc(th)}</span></p>
        ${beads(n, g.res, -1)}
        ${best}
        <div class="actions">
          ${sug[0] ? `<button class="btn gold next-set" data-play="${esc(sug[0])}"><span>Try another set <span class="th" lang="th">ลองชุดถัดไป</span> ▸</span><small>${esc(titleOf(sug[0]))}</small></button>` : ''}
          <div class="split">
            <button class="btn ghost" data-act="again">↻ Play again</button>
            <button class="btn ghost" data-act="home">All sets</button>
          </div>
        </div>
        ${sug.length > 1 ? `<section class="box"><h3>Or try <small class="th" lang="th">หรือลองชุดนี้</small></h3>
          <div class="rows">${sug.slice(1).map((id) => row(id, partOf(id), titleOf(id), esc(subOf(id)))).join('')}</div></section>` : ''}
        <section class="box">
          <h3>${misses.length ? `Check your mistakes <small class="th" lang="th">ทบทวนข้อที่ตอบผิด (${misses.length})</small>` : 'Mistakes'}</h3>
          ${misses.length ? `<ul class="mist">${misses.map(({q, i}) => `<li>
              <span class="mq">${i + 1}. ${fmt(q.q)}</span>
              <span class="mine">✗ ${esc(q.opts[g.pick[i]].t)}</span>
              <span class="ok">✓ ${esc(q.opts.find((o) => o.right).t)}</span>
              <p class="fb-ex" lang="th">${fmt(q.ex)}</p></li>`).join('')}</ul>`
            : '<p class="allright">None — every answer was right! <span class="th" lang="th">ถูกทุกข้อ เยี่ยมมาก</span></p>'}
        </section>
      </section>`;
  }

  // ── events ────────────────────────────────────────────────────────────
  app.addEventListener('click', (e) => {
    const t = e.target.closest('[data-k],[data-act],[data-play]');
    if (!t) return;
    if (t.dataset.k !== undefined) return answer(Number(t.dataset.k));
    if (t.dataset.play) return start(t.dataset.play, false);
    switch (t.dataset.act) {
      case 'next': return next();
      case 'quit': return renderHome();
      case 'resume': return renderQuestionResume();
      case 'again': return start(game.id, true);
      case 'home': game = null; return renderHome();
      case 'name': return renderWelcome();
    }
  });
  function renderQuestionResume() {
    const answered = game.answered;
    const k = game.pick[game.i];
    renderQuestion();
    if (answered) {
      // show the same answer + explanation again without counting it twice
      if (game.res[game.i]) game.streak -= 1;
      game.answered = false;
      game.res[game.i] = undefined;
      answer(k);
    }
  }
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

  if (store.name) renderHome();
  else renderWelcome();
})();
