# LOOP ENGINEERING — swipe
*@jaiden.rabatin · the agent loop, for real*

**Comment `LOOPS`** and I'll DM you the full breakdown.  ·  Full guide: https://jaidenrabatin.com/guides/loop-engineering.html

---

### 1 · Hook

# YOU'RE NOT PROMPTING. YOU'RE RUNNING A LOOP.

Every Claude Code run is the same 5-stage loop. Control it and it works while you sleep.

`AGENT SDK` · `REAL MECHANICS` · `I RUN THIS DAILY`

---

### 2 · STEP 01 — The loop, exactly

- Receive prompt -> evaluate -> call tools -> feed results back -> repeat.
- Each full cycle is one turn. It ends only when Claude replies with no tool calls.
- This isn't a metaphor — it's the documented execution loop in the Agent SDK.

> **I pointed this loop at my whole site: 'reformat every page.' It looped file-by-file until done.**

```
# the agent loop
1 receive prompt
2 evaluate + respond
3 execute tools
4 repeat  (= one turn)
5 return result
```

---

### 3 · STEP 02 — A turn is the unit

- One turn = Claude calls tools, the SDK runs them, results return — no stop for you.
- It streams messages: System(init) -> Assistant -> User(tool result) -> Result.
- 'Fix the failing tests' is just a few turns chained together.

> **My debugging loop: run tests, read the files, edit + re-run, report. 4 turns, zero babysitting.**

```
# fix auth.ts (4 turns)
t1 bash: npm test -> 3 fail
t2 read auth.ts + test
t3 edit + re-run -> pass
t4 'fixed, 3/3 green'
```

---

### 4 · STEP 03 — Put a leash on it

- No limits = it runs till done. Great when scoped, risky on 'improve this codebase.'
- max_turns and max_budget_usd cap it. effort dials reasoning: low -> max.
- A budget is the right default for anything autonomous.

> **I cap turns so a debugging loop can't spiral, and raise effort only for the hard refactors.**

```
# ClaudeAgentOptions
max_turns = 30
max_budget_usd = 2.00
effort = 'high'
(low / medium / high / max)
```

---

### 5 · STEP 04 — Why long loops get dumb

- Context never resets — history + tool outputs pile up.
- Near the limit it auto-compacts; early orders can drop.
- Fix: put persistent rules in CLAUDE.md, re-sent every request.

> **Reformatting 29 pages blew context fast — I moved the format spec to CLAUDE.md so every loop kept the rules.**

```
# context discipline
history grows every turn
system: compact_boundary
rules -> CLAUDE.md (sticky)
subagents for big subtasks
```

---

### 6 · STEP 05 — Let it act safely

- allowed_tools auto-approves; disallowed_tools blocks.
- Read-only tools run in parallel; writes run one at a time.
- Hooks (PreToolUse/PostToolUse) validate or block — off the context.

> **In code review I run acceptEdits with a PreToolUse hook that blocks anything touching files outside the repo.**

```
# guardrails
allowed: Read Edit Bash Glob
permission_mode: acceptEdits
hook PreToolUse -> block rm -rf
denied -> Claude reroutes
```

---

### 7 · STEP 06 — Know when it stopped

- The loop ends with a ResultMessage — check subtype first.
- success / error_max_turns / error_max_budget_usd.
- Capture session_id to resume right where it stopped.

> **Hit the turn limit mid-debug? Resume the session. No re-explaining — it remembers every file it read.**

```
# handle the result
if subtype == success:
  use result
elif error_max_turns:
  resume(session_id)
```

---

### 8 · CTA

**Comment `LOOPS`** — I'll DM you the Agent Loop Control Sheet — every knob (turns, budget, effort, permissions, hooks, result codes) on one page.

Follow @jaiden.rabatin for the AI systems I actually run — grounded in the real docs, not vibes.
