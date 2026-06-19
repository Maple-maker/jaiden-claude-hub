# War Loops — Scorecard

Direction: **Redacted Field Manual** · Branch: `redesign/field-manual`
Judge axes scored 0–10. Pass = ≥8 on all three. Each cron cycle: read this file, repair the
single top item in **NEXT ACTIONS**, re-render, re-score, append a cycle entry, commit.

Capture note: headless Chrome has a ~500px minimum window width, so true ≤500px phone widths
are validated by **code review** (overflow guard + `@media(max-width:440px)`), not pixel capture.
Trustworthy pixel renders: 1440 / 768 / 500.

---

## Current scores — index.html (the mockup)

| Axis | Score | Notes |
|------|-------|-------|
| Static design | 9 / 10 | Exact palette + all 4 fonts. Manifest bar, corner brackets, SEC numbering, redaction reveal, mono keywords, Playfair quote, single warm-light glow. Orange well under 10%. Batman test passes. |
| Experiential motion | 8 / 10 | Redaction declassify, staggered scroll fade-up, blinking cursor, live section counter, 200–300ms hover. `prefers-reduced-motion` fully guarded. Calm + hard-edged per brand (restraint intentional). |
| Responsive reflow | 8 / 10 | Clean at 1440 / 768 / 500: 2-col→1-col grid, manifest wraps, buttons wrap. Sub-500 covered by code, not pixel-verified (capture floor). |

**index.html verdict: PASS** (all axes ≥8) — established as the design-system reference.

---

## NEXT ACTIONS (work queue — top item is next cycle's target)

The mockup passes, but the **site does not yet match site-wide**. Remaining highest-impact gaps,
in priority order:

1. **404.html** — restyle to Field Manual (quick, high visibility).
2. **guides/*.html** (18 pages) — propagate design system: tokens, fonts, manifest bar,
   SEC headers, bracket styling, reduced-motion. One page per cycle, simplest first
   (skills-101 → skill-creator → …). Verify each renders.
3. **posts/*.html** (18 carousel pages) — same propagation pass.
4. **blog/the-real-agi-race.html** — long-form reading layout in Field Manual style
   (measure ≤72ch, Playfair pull-quotes, mono captions).
5. Cross-page polish: shared header/footer consistency, `<title>`/OG parity, sitemap unaffected.

Extract the locked CSS tokens block + manifest/section partial from index.html as the
copy-source for every propagation cycle. Keep all existing content, links, and SEO/meta intact.

---

## Cycle log

### Cycle 00 — 2026-06-19 — FOUNDATION
- Cloned repo, read brand guidelines, locked **Redacted Field Manual** direction (user choice).
- Wrote ground-truth spec (`.warloops/spec.md`).
- Rebuilt `index.html`: brand tokens, 4-font system, manifest bar, redaction-reveal hero,
  mono command-line, SEC 01/02 numbered sections, bracket cards w/ mono keywords, warm-light
  glow, scroll-reveal + live counter, full reduced-motion guard. Replaced all emoji glyphs with SVG.
- Captured renders (1440 / 768 / 500). Surgical repair: manifest wrap + stamp-hide <440 +
  overflow-x guard (fixed a real narrow-width bleed; the 375 "overflow" seen first was a
  headless-capture artifact).
- Preserved 1 deep dive + 18 guides + 18 carousel links + SEO/meta/JSON-LD.
- index.html PASSES all three axes. Site-wide propagation pending (see NEXT ACTIONS).
