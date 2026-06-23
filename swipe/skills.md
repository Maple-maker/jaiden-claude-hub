# SKILLS — swipe
*@jaiden.rabatin · teach it once*

**Comment `SKILLS`** and I'll DM you the full breakdown.  ·  Full guide: https://jaidenrabatin.com/guides/skills.html

---

### 1 · Hook

# STOP RE-EXPLAINING YOUR WORKFLOW.

Teach Claude your process once. It runs it on command, forever.

`DO IT ONCE` · `AUTO-TRIGGERS` · `REUSABLE`

---

### 2 · STEP 01 — What a skill is

- A skill is a folder with a SKILL.md Claude loads on demand.
- It packages your workflow — steps, rules, examples — into one command.
- Write it once; stop re-explaining the same process every session.

> **A prompt is a one-off. A skill is a process you keep.**

```
# skills/
skills/
  brand-guidelines/SKILL.md
  weekly-report/SKILL.md
  carousel-studio/SKILL.md
```

---

### 3 · STEP 02 — How it triggers

- Each skill has a description with trigger phrases.
- Claude reads it and fires the skill when your ask matches.
- No slash command needed — though you can call it by name.

> **You describe when to use it. Claude decides to reach for it.**

```
# auto-trigger
description: use when...
> make me a carousel
matched -> skill loads
```

---

### 4 · STEP 03 — What goes inside

- Frontmatter: a name + a sharp description (the trigger).
- Body: the steps, the rules, and what 'done' looks like.
- Point it at any scripts or templates it should use.

> **Write it for a smart new teammate: clear steps, no guessing.**

```
# SKILL.md
---
name: weekly-report
description: use when...
---
## steps
```

---

### 5 · STEP 04 — Make it reliable

- Add a verification step so the skill checks its own work.
- Bake in your standards; catch mistakes before they ship.
- A skill that self-checks beats one that just hopes.

> **The best skills end by proving they did it right.**

```
# verify
## verify
- dims correct?
- on brand?
PASS -> deliver
```

---

### 6 · STEP 05 — Build your first one

- Start from a task you repeat every week.
- Write the steps you'd tell a new hire, save as SKILL.md.
- Turn it on in Settings -> Capabilities and run it.

> **If you've explained it twice, it should be a skill.**

```
# ship it
> settings > capabilities
skill: ON
> run it
```

---

### 7 · CTA

**Comment `SKILLS`** — I'll DM you a fill-in-the-blank SKILL.md starter + how to wire it in.

Follow @jaiden.rabatin for AI systems that do real work — the stack I actually run.
