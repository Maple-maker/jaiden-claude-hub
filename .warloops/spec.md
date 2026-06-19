# War Loops — Ground-Truth Design Spec

> Target: revamp `jaiden-claude-hub` to the Jaiden Rabatin personal brand.
> Source of truth: `/Users/jaidenrabatin/Downloads/Jaiden Rabatin personal brand/jaiden_rabatin_brand_guidelines_v2.md`
> Direction (locked 2026-06-19): **Redacted Field Manual** — military declassified-brief aesthetic.

## Aesthetic
Quiet Operator. One warm light in a dark room. A declassified field manual on a clean desk.
Calm, convicted, minimal. Not influencer, not tactical-cosplay. The "Batman test": if it
wouldn't sit next to a silhouette-Bruce-Wayne-with-a-book image, it's wrong.

## Color tokens (LOCKED — hex must match exactly)
| Token | Hex | Use |
|-------|-----|-----|
| Obsidian | `#0B0B0B` | default background |
| Carbon | `#1A1A1A` | cards / secondary surface |
| Bone | `#F4F1EA` | default text on dark |
| Signal Orange | `#C4522A` | brand accent — **≤10% of any frame**, one element per region |
| Field Tan | `#C2A878` | warmth, secondary highlight, rules |
| Ash | `#6B6B6B` | captions, metadata, muted text |
| Olive Drab | `#4B5320` | sparingly, military reference moments only |

Rules: black + bone dominate. Orange is an accent, never the identity. Hard edges — no
gradient orange into other colors. No neon, no fintech blue, no red (except warning/debt).
Max contrast: bone on obsidian, never grey-on-grey.

## Typography (LOCKED)
| Use | Font | Weight |
|-----|------|--------|
| Headlines | Barlow Condensed | 900 (command voice, thesis statements) |
| Subheads | Playfair Display | 700 (sparingly — one drop of gravity) |
| Body | DM Sans | 400 / 500 |
| Labels / data / code | DM Mono | 500 (dates, ratios, system names, keywords) |

UPPERCASE reserved for labels (FIELD NOTE, SEC 01, CLASSIFIED). Text fills the frame —
big and confident, never timid in a corner. No script fonts. No decorative serifs.

## Field-Manual motifs
- Top "manifest" bar: `FIELD MANUAL // CLASSIFIED`, `J. RABATIN // CLAUDE OPS`, with corner brackets `⌐ ⌐`.
- Hero headline with a redaction bar that reveals a word on load (motion, reduced-motion safe).
- Mono command-line subtitle with a blinking cursor.
- Sections numbered `SEC 01`, `SEC 02` … with thin Field-Tan rules and mono labels.
- Guide cards: corner brackets, mono keyword tag (ENABLE / CREATOR / TRIGGER …) right-aligned.
- Index counter `01 / 18` style in mono ash.

## Motion
- Hero redaction reveal on load (~600ms, ease-out).
- Scroll-reveal fade-up for cards via IntersectionObserver, staggered.
- Hover: color/border/opacity transitions 200–300ms. No layout-shifting scale transforms.
- Blinking cursor on the command subtitle.
- **MUST** respect `prefers-reduced-motion: reduce` (all entrance/cursor animation off).

## Hard requirements (non-negotiable)
- No emojis as icons — inline SVG only (replace ↓ ▶ ☀ glyphs).
- Touch targets ≥44px; focus-visible rings; aria-labels on icon-only controls.
- Body text ≥16px on mobile; no horizontal scroll at 375 / 768 / 1024 / 1440.
- Preserve all existing content: 1 deep dive + 18 guides + carousel/keyword links + SEO/meta/JSON-LD.
- Keep regulatory/positioning copy intact.

## Judge axes (each scored 0–10; pass = ≥8 all three)
1. **Static design** — palette/type/aesthetic fidelity to brand + Batman test.
2. **Experiential motion** — calm, hard-edged, reduced-motion safe; nothing flashy.
3. **Responsive reflow** — clean at 375 / 768 / 1024 / 1440, no overflow, readable.

## Stop conditions
Scores plateau across 2 cycles · all three axes ≥8 · capture blocked.
