# Click-through software simulation (GitHub Pages)

A tiny, dependency-free player for "Show me / Try me" software simulations, plus a console script that
captures an SAP Enable Now simulation into the format the player reads.

Demo content: **Create a Contract Workspace** (SAP Ariba), 36 steps.

## Files

| File | What it is |
|---|---|
| `index.html` | The player. One file, no build step. Reads `sim.json`. |
| `sim.json` | The steps: type (`info` / `click` / `input`), screenshot id, target box, bubble text, expected input. |
| `img/` | Optional local screenshots (`<id>.jpg`). If a file is missing the player falls back to the remote original. |
| `tools/extract-enablenow.js` | Paste in DevTools on an Enable Now simulation. Replays it and downloads `sim-kit.zip` (`sim.json` + `img/`). |

## Publish

1. Put these files in a repo (root or a sub-folder).
2. Settings → Pages → deploy from the branch.
3. Open `https://<user>.github.io/<repo>/`. Progress is remembered per browser.

Run locally with `python3 -m http.server` (opening `index.html` from disk can't load `sim.json`).

## Capture a new simulation

1. Open the simulation link in Chrome, wait until step 1 shows (use **Restart** if it resumed mid-way).
2. DevTools → Console → paste `tools/extract-enablenow.js` → Enter. It plays itself (~1.5 s/step).
3. A `sim-kit.zip` downloads. Unzip it over this folder (replaces `sim.json`, adds `img/`).
4. Check any step flagged `"inferred": true` in `sim.json`. These have icon-only labels like "Click ." in the original.

## How it works (what was learned from the original)

* Each step is a full-screen screenshot plus overlay objects: a **Bubble** (instruction), a **hotspot** over the real UI
  element (click targets, radio buttons, dropdowns) or an **input box**, and a highlight outline.
* Screenshots are shared between steps: several steps can sit on the same image (`macro/MAC_<id>/dump_page<N>/img.png`).
* Coordinates are in a 1309 × 676 stage; the player scales it to the window.
* Step types: `info` (read, press ▶), `click` (click the highlighted area; a miss shakes it), `input` (type the bold text,
  case-insensitive; "Fill it in for me" is the hint).

## Content and copyright

The player and extractor are generic. The captured screenshots and text in a captured simulation belong to
their owner (here SAP). Keep captured SAP content for personal study or get permission before publishing it publicly.
For public sites, build `sim.json` + screenshots from your own system recordings.
