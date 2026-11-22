/* extract-enablenow.js
 * Paste into the browser DevTools console on an SAP Enable Now "Trainer" simulation page
 * (URL like .../pub/<tenant>/index.html?show=project!PR_xxx:uebung), with the simulation at its FIRST step
 * (use the Restart link if it resumed somewhere else). It replays the whole walkthrough by itself,
 * records every step, then downloads  sim-kit.zip  =  sim.json + img/*.jpg  for the player in this repo.
 *
 * Needs ~1.4 s per step (a 36-step demo takes about a minute). Nothing is sent anywhere.
 * Tip: window.__sim holds the result; run  __sim.steps.filter(s=>s.inferred)  to see steps worth a manual check.
 */
(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const IMG_RE = /^(.*\/macro\/)MAC_([0-9A-Fa-f]+)\/dump_page(\d+)\/img\.png$/;
  const MAX_STEPS = 400;

  // ---- read the current slide (the player renders each slide in a same-origin iframe) -------------------
  function snap() {
    const f = document.querySelector('iframe'); if (!f) return null;
    const d = f.contentDocument, w = f.contentWindow; if (!d) return null;
    const cvEl = d.getElementById('canvas'); if (!cvEl) return null;
    const cv = cvEl.getBoundingClientRect();
    const rel = b => [b.x - cv.x, b.y - cv.y, b.width, b.height].map(Math.round);
    const bgi = d.querySelector('img'); if (!bgi) return null;
    const m = IMG_RE.exec(bgi.src.split('?')[0]); if (!m) return { end: true };   // start/end screens use theme images
    const bubbleEls = [...d.querySelectorAll('div.Bubble')].filter(b => b.getBoundingClientRect().width > 0);
    const bubbles = bubbleEls.map(b => {
      const same = [...d.querySelectorAll('[id="' + b.id + '"]')];
      const text = same.map(e => e.innerText || '').join(' ').replace(/\s+/g, ' ').trim();
      let bold = same.flatMap(e => [...e.querySelectorAll('b,strong,[style*="bold"]')]).map(e => e.innerText.replace(/\s+/g, ' ').trim()).filter(Boolean);
      if (bold.length > 1 && /\bin the\b.*\b(box|field)\b/i.test(text)) bold = bold.slice(0, -1);   // drop the field label
      return { box: rel(b.getBoundingClientRect()), text, bold };
    }).filter(b => b.text);
    const inside = (a, r) => a.x >= r.x - 2 && a.right <= r.right + 2 && a.y >= r.y - 2 && a.bottom <= r.bottom + 2;
    const arrow = [...d.querySelectorAll('#canvas a')].find(a => { const b = a.getBoundingClientRect(); return b.width > 0 && bubbleEls.some(x => inside(b, x.getBoundingClientRect())); });
    const ctls = [...d.querySelectorAll('#canvas div[class*="Control"]')].filter(e => !/Poi/.test(e.className) && e.getBoundingClientRect().width > 0);
    const inp = d.querySelector('input.InputTextControl,textarea.InputTextControl');
    const type = arrow ? 'info' : inp ? 'input' : ctls.length ? 'click' : 'other';
    return {
      d, w, arrow, ctls, inp, stage: [Math.round(cv.width), Math.round(cv.height)], base: m[1], mac: m[2], page: m[3],
      rec: {
        t: type, img: m[2] + '_' + m[3], bubbles,
        target: type === 'input' ? rel(inp.getBoundingClientRect()) : type === 'click' ? rel(ctls[0].getBoundingClientRect()) : null,
      },
    };
  }
  const fire = (w, el, types, extra = {}) => types.forEach(t => el.dispatchEvent(new w.MouseEvent(t, { bubbles: true, cancelable: true, view: w, ...extra })));

  // ---- replay ------------------------------------------------------------------------------------------------
  const steps = []; let base = '', stage = [1309, 676], stall = 0, started = false;
  for (let i = 0; i < MAX_STEPS; i++) {
    let S; try { S = snap(); } catch (e) { S = null; }
    if (!S) { await sleep(700); continue; }
    if (S.end) { if (started) break; await sleep(700); continue; }
    started = true; base = S.base; stage = S.stage;
    // wait (max ~3 s) until the bubble text has rendered
    for (let k = 0; k < 6 && !S.rec.bubbles.length && S.rec.t !== 'other'; k++) { await sleep(500); try { S = snap() || S; } catch (e) {} }
    const r = S.rec, last = steps[steps.length - 1];
    const sameSlot = last && last.img === r.img && last.t === r.t && JSON.stringify(last.target) === JSON.stringify(r.target);
    if (!sameSlot) { steps.push(r); stall = 0; }
    else if (last.bubbles.map(b => b.text).join() !== r.bubbles.map(b => b.text).join()) { steps[steps.length - 1] = r; stall = 0; }
    else if (++stall >= 3) { console.warn('Stalled on step', steps.length, '- stopping.'); break; }
    if (S.arrow) fire(S.w, S.arrow, ['click']);
    else if (S.inp) {
      const exp = r.bubbles.flatMap(b => b.bold).join(' ').trim(); steps[steps.length - 1].expected = exp;
      const el = S.inp; el.focus();
      for (const ch of exp) { el.value += ch; ['keydown', 'keypress', 'input', 'keyup'].forEach(t => el.dispatchEvent(new S.w.KeyboardEvent(t, { key: ch, bubbles: true }))); }
      await sleep(250);
      ['keydown', 'keyup'].forEach(t => el.dispatchEvent(new S.w.KeyboardEvent(t, { key: 'Enter', keyCode: 13, which: 13, bubbles: true })));
    } else if (S.ctls.length) {
      const b = S.ctls[0].getBoundingClientRect(), x = b.x + b.width / 2, y = b.y + b.height / 2;
      fire(S.w, S.d.elementFromPoint(x, y) || S.d.body, ['mousedown', 'mouseup', 'click'], { clientX: x, clientY: y });
    } else { await sleep(900); continue; }
    await sleep(1400);
  }
  if (!steps.length) { console.error('No steps captured - is the simulation open on its first step?'); return; }

  // ---- shape the result ----------------------------------------------------------------------------------------
  const title = (document.querySelector('h1') || {}).innerText || document.title || 'Simulation';
  const sim = {
    title: title.trim(), source: 'SAP Enable Now Trainer simulation', stage, remoteBase: base, remotePattern: 'MAC_{mac}/dump_page{page}/img.png',
    steps: steps.map(s => {
      const b = s.bubbles[0], o = { t: s.t, img: s.img };
      if (s.target) o.target = s.target;
      o.bubble = { text: b ? b.text : '' }; if (b) o.bubble.box = b.box;
      if (s.expected) o.expected = s.expected;
      if (!b || /(^|\s)(Click|Select)\s*\.$/.test(b.text) || !b.text) o.inferred = true;   // icon-only labels / bubble never rendered
      return o;
    }),
  };
  window.__sim = sim;
  const odd = sim.steps.map((s, i) => s.inferred ? i + 1 : 0).filter(Boolean);
  console.log('Captured', sim.steps.length, 'steps.', odd.length ? 'Check wording of steps: ' + odd.join(', ') : 'All bubble texts read cleanly.');

  // ---- images -> small JPEGs, then a zip (store only) ----------------------------------------------------------------
  const files = [{ name: 'sim.json', data: new TextEncoder().encode(JSON.stringify(sim, null, 1)) }];
  for (const id of [...new Set(sim.steps.map(s => s.img))]) {
    const [mac, page] = id.split('_');
    try {
      const resp = await fetch(base + 'MAC_' + mac + '/dump_page' + page + '/img.png'); if (!resp.ok) throw new Error(resp.status);
      const bmp = await createImageBitmap(await resp.blob());
      const sc = Math.min(1, 1400 / bmp.width), c = document.createElement('canvas'); c.width = Math.round(bmp.width * sc); c.height = Math.round(bmp.height * sc);
      c.getContext('2d').drawImage(bmp, 0, 0, c.width, c.height);
      const blob = await new Promise(r => c.toBlob(r, 'image/jpeg', 0.78));
      files.push({ name: 'img/' + id + '.jpg', data: new Uint8Array(await blob.arrayBuffer()) });
    } catch (e) { console.warn('image failed', id, e); }
  }
  // ZIP-BEGIN
  const crcTable = (() => { const t = new Uint32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
  const crc32 = u8 => { let c = 0xFFFFFFFF; for (let i = 0; i < u8.length; i++) c = crcTable[(c ^ u8[i]) & 0xFF] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; };
  function makeZip(files) {
    const enc = new TextEncoder(), parts = [], central = []; let offset = 0;
    const now = new Date(), dt = ((now.getHours() << 11) | (now.getMinutes() << 5) | (now.getSeconds() >> 1)) & 0xFFFF, dd = (((now.getFullYear() - 1980) << 9) | ((now.getMonth() + 1) << 5) | now.getDate()) & 0xFFFF;
    for (const f of files) {
      const name = enc.encode(f.name), crc = crc32(f.data), size = f.data.length;
      const lh = new DataView(new ArrayBuffer(30));
      lh.setUint32(0, 0x04034b50, true); lh.setUint16(4, 20, true); lh.setUint16(6, 0x0800, true); lh.setUint16(8, 0, true); lh.setUint16(10, dt, true); lh.setUint16(12, dd, true);
      lh.setUint32(14, crc, true); lh.setUint32(18, size, true); lh.setUint32(22, size, true); lh.setUint16(26, name.length, true); lh.setUint16(28, 0, true);
      parts.push(new Uint8Array(lh.buffer), name, f.data);
      const ch = new DataView(new ArrayBuffer(46));
      ch.setUint32(0, 0x02014b50, true); ch.setUint16(4, 20, true); ch.setUint16(6, 20, true); ch.setUint16(8, 0x0800, true); ch.setUint16(10, 0, true); ch.setUint16(12, dt, true); ch.setUint16(14, dd, true);
      ch.setUint32(16, crc, true); ch.setUint32(20, size, true); ch.setUint32(24, size, true); ch.setUint16(28, name.length, true); ch.setUint32(42, offset, true);
      central.push(new Uint8Array(ch.buffer), name);
      offset += 30 + name.length + size;
    }
    const cdSize = central.reduce((a, b) => a + b.length, 0), end = new DataView(new ArrayBuffer(22));
    end.setUint32(0, 0x06054b50, true); end.setUint16(8, files.length, true); end.setUint16(10, files.length, true); end.setUint32(12, cdSize, true); end.setUint32(16, offset, true);
    return new Blob([...parts, ...central, new Uint8Array(end.buffer)], { type: 'application/zip' });
  }
  // ZIP-END
  const url = URL.createObjectURL(makeZip(files)), a = document.createElement('a');
  a.href = url; a.download = 'sim-kit.zip'; document.body.appendChild(a); a.click(); a.remove();
  console.log('Downloaded sim-kit.zip -> unzip into the repo root next to index.html (sim.json + img/).');
})();
