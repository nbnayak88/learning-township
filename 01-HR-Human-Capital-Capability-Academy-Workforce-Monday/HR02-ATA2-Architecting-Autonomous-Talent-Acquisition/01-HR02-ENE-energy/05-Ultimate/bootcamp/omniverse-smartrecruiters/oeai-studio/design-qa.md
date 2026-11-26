# OEAI Studio design and functional QA

Date: 26 November 2026.

## Verified

- All 17 positions navigated in the browser in sequence. Local counts 5/3/4/5 and overall counters matched the visible views.
- Initial Previous disabled; final Next disabled. Chapter boundaries traversed forward; direct preview and evaluation selection worked.
- Restart returned to position 1.
- Approved synthetic inputs returned the expected evidence-linked draft.
- Publish request was blocked in browser; no external write.
- Ten deterministic guard cases passed in Node and browser. Baseline draft smoke check passed in Node.
- Enlarge, zoom and Close worked.
- Desktop positions had no horizontal page overflow.
- 390 × 844 CSS-pixel iframe inspected; its effective content width was 375px with scrollWidth 375px. Preview remained reachable. This is an embedded viewport check, not a physical-device test.
- Original source skill and PRM-OVE-181/182 retained in the pack.
- Logo, lime/green header, Comfortaa and reading bar present.

## Limits

This is an independent adaptation with original OEAI screens. It is not a pixel-equivalent SAP clone and contains no relabelled SAP screenshots. No tenant, language model, identity provider, production API or external workflow has been exercised. Model evaluation, adverse-impact analysis and integration evidence remain required. Local adapter names are proposed contracts. Downloaded screen SVG uses foreignObject; viewer support varies. Comfortaa uses Google Fonts and requires network access, with a system fallback.

Browser-extension metadata errors were observed from a chrome-extension origin. No application-origin JavaScript error was observed in the tested interactions.
