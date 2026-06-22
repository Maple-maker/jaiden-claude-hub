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

Site is now on-brand across **index + 404 + all 20 guides + all 18 posts + blog (incl. charts)**.

**SITE VERDICT: PASS — site-wide propagation complete.** Scores have plateaued at 9/8/8 and all
three axes pass; no high-impact gap remains. Recommend stopping the loop (CronDelete f364b8b0).

Optional future polish (low impact, not loop-worthy): `<title>`/OG-tag parity across guide pages,
shared header/footer extraction, blog inline-SVG `prefers-reduced-motion` audit.

_Done: 404 (c01) · skills-101=template (c02) · skill-creator (c03) · trigger-design (c04) ·
chat-to-skill (c05) · ALL 20 guides + ALL 18 posts (c06 BATCH) · blog charts (c07)._

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

### Cycle 01 — 2026-06-19 — 404.html
- Surgical critic top gap: 404.html was a single-line page with off-brand hex
  (#0D0D0D / #F2EDE4 / #E8784A) — visually broke from the new homepage.
- Rebuilt to Field Manual: brand tokens, Barlow/DM Sans/DM Mono, warm-light glow,
  corner-bracket `SIGNAL LOST` tag, Barlow 404, mono command-line w/ cursor, single
  orange CTA, reduced-motion guard. Rendered at 1024 — on-brand, consistent w/ index.
- Scores hold (Static 9 / Motion 8 / Responsive 8). No regression. Loop continues:
  next gap = guides/*.html propagation (start skills-101).

### Cycle 02 — 2026-06-19 — guides/skills-101.html (TEMPLATE)
- Surgical critic top gap: guide pages were a separate light theme (#FAFAFA, Inter +
  JetBrains Mono, amber #C8860A, green/blue/red callouts) — total break from the dark
  Field Manual homepage.
- Converted skills-101.html → guide-page template: brand tokens, 4-font system, manifest
  bar w/ back-link, bracketed TOC + mono numbering, SECTION rules, restrained callouts
  (orange/olive/tan/muted-danger), dark code blocks, SVG download icon, reduced-motion guard.
- Preserved all body copy, the 10-item grid, and the download script verbatim (downloadAsset
  + checklist). Rendered at 900w — on-brand, consistent w/ index + 404.
- Scores hold (9 / 8 / 8). Loop continues: 15 linked guides (+2 unlinked) copy this template,
  next = skill-creator.

### Cycle 03 — 2026-06-19 — guides/skill-creator.html
- Applied the cycle-02 guide template to skill-creator.html (was still the old light theme).
- Swapped CSS/shell to Field Manual; kept all body copy, the 10-item download grid, the
  SKILL.md frontmatter starter, and downloadAsset() (SKILL-template.md) verbatim. Rendered
  at 900w — matches template. Scores hold (9 / 8 / 8). Next = trigger-design.

### Cycle 04 — 2026-06-19 — guides/trigger-design.html (+ tool)
- Built `.warloops/apply_template.py`: deterministic guide converter (swaps fonts + style +
  injects manifest + replaces download arrow; never touches body copy or download script).
  Extracts the locked style/manifest from skills-101.html so there is zero drift.
- Ran it on trigger-design.html. Validated (no off-brand leftovers, 4 fonts, manifest, reduced
  motion, download intact, 4 sections) + rendered at 900w — matches template. Scores hold (9/8/8).
- This tool makes remaining guides one-command each (and a "batch the rest" trivial).
  Next = chat-to-skill.

### Cycle 05 — 2026-06-19 — guides/chat-to-skill.html
- Ran apply_template.py on chat-to-skill.html. Validated (no off-brand leftovers, 4 fonts,
  manifest, reduced motion, download intact, glyph gone, 4 sections) + rendered at 900w —
  matches template. Scores hold (9 / 8 / 8). Next = skills-to-plugin.

### Cycle 06 — 2026-06-19 — BATCH (user: "batch the rest")
- Guides: converted the remaining 16 via apply_template.py (per-file loop; zsh doesn't
  word-split unquoted vars). All 20 guides validated (0 failing): no off-brand leftovers,
  brand tokens, 4 fonts, manifest, download script intact, arrow glyph gone. Spot-rendered
  the two structural outliers (claude-vs-chatgpt, tips-5-illegal — custom ROUND/TIP section
  labels) + dynamic-workflows: clean.
- Posts: the 18 carousels were already in the brand system (4 fonts, #C4522A) but on legacy
  base hex. Aligned #0D0D0D→#0B0B0B and #F2EDE4→#F4F1EA across all 18 (vars in :root, one
  edit covers each). Rendered skills-101 + loop-engineering (React mounts): on exact tokens.
  Note: carousels run heavier orange by design (Instagram medium); the ≤10% rule governs
  website frames, not slide art. Minor deferred: #E8784A orange-light tint left as-is.
- Scores hold (Static 9 / Motion 8 / Responsive 8). Remaining: blog long-form + polish.

### Cycle 07 — 2026-06-19 — blog/the-real-agi-race.html (charts)
- Surgical critic top gap: blog inline-SVG figures used 5 off-brand data hues (blue #6E97C4,
  gold #E0A33D, green #6FAE6B, red #D9663F, orange-light #E8784A) — fintech-blue violated brand.
- Remapped each to the nearest locked token: orange-light→#C4522A (Signal Orange), amber→#C2A878
  (Field Tan), green→#8A9657 (olive tint), blue→#6B6B6B (Ash, kills the blue), red→#9C4A3A
  (muted danger). #C4522A was only a var def (no series), so no collisions.
- Rendered full page + cropped 3 chart bands: exponential line (orange + tan marker), 5%-compute
  bar chart (orange bars + tan callout), callouts (mono labels) — all legible + on-brand.
- Scores hold (9 / 8 / 8). SITE-WIDE PROPAGATION COMPLETE → recommend stopping the loop.
