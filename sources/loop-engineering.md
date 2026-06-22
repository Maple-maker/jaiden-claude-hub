# Sources — Loop Engineering / "How the agent loop works"

**Post:** Loop engineering: how the agent loop actually works
**Author:** Jaiden Rabatin (@jaiden.rabatin)
**Compiled / verified:** 2026-06-22
**Method:** Primary content taken verbatim-in-meaning from Anthropic's official Agent SDK
documentation. The primary page was fetched live and confirmed identical to the captured
source on the verification date.

---

## Primary source

- **How the agent loop works** — Agent SDK docs (canonical for this post)
  https://code.claude.com/docs/en/agent-sdk/agent-loop
  Mirror: https://platform.claude.com/docs/en/agent-sdk/agent-loop

## Supporting official sources

- How Claude Code works — the agentic loop (conceptual)
  https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop
- Hooks (PreToolUse, PostToolUse, Stop, PreCompact, subagent hooks)
  https://code.claude.com/docs/en/agent-sdk/hooks
- Permissions (allow/deny order, rule syntax like `Bash(npm *)`)
  https://code.claude.com/docs/en/agent-sdk/permissions
- Subagents (fresh context, what subagents inherit)
  https://code.claude.com/docs/en/agent-sdk/subagents
- Sessions (resume, continue, fork)
  https://code.claude.com/docs/en/agent-sdk/sessions
- Effort (which models support it; levels)
  https://platform.claude.com/docs/en/build-with-claude/effort
- Prompt caching (stable prefixes cached across turns)
  https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Models (IDs, e.g. claude-sonnet-4-6)
  https://platform.claude.com/docs/en/about-claude/models
- Python message types reference
  https://code.claude.com/docs/en/agent-sdk/python#message-types
- TypeScript message types reference
  https://code.claude.com/docs/en/agent-sdk/typescript#message-types

---

## Claim → source map (every factual claim on the page)

| # | Claim in the post/guide | Source |
|---|---|---|
| 1 | The SDK runs the same execution loop that powers Claude Code; 5 stages: receive → evaluate → execute tools → repeat → return result | agent-loop · "The loop at a glance" |
| 2 | Each full cycle is one turn; loop ends when Claude responds with no tool calls | agent-loop · "Turns and messages" |
| 3 | "Fix the failing tests in auth.ts" = 4 turns (test, read, edit+rerun, summary) | agent-loop · "Turns and messages" |
| 4 | Five core message types: SystemMessage, AssistantMessage, UserMessage, StreamEvent, ResultMessage | agent-loop · "Message types" |
| 5 | SystemMessage subtypes: init, compact_boundary, informational, worker_shutting_down | agent-loop · "Message types" |
| 6 | `max_turns`/`maxTurns` caps tool-use round trips; `max_budget_usd`/`maxBudgetUsd` caps spend; no limit by default | agent-loop · "Turns and budget" |
| 7 | Hitting a cap → ResultMessage subtype `error_max_turns` / `error_max_budget_usd` | agent-loop · "Turns and budget" / "Handle the result" |
| 8 | `effort` levels: low, medium, high, xhigh, max; independent from extended thinking | agent-loop · "Effort level" |
| 9 | Context window does not reset between turns; everything accumulates; large tool outputs are costly | agent-loop · "The context window" |
| 10 | Automatic compaction summarizes old history near the limit; emits `compact_boundary`; early instructions can drop | agent-loop · "Automatic compaction" |
| 11 | Persistent rules belong in CLAUDE.md (re-injected every request, prompt-cached) | agent-loop · "Automatic compaction" / "What consumes context" |
| 12 | Subagents start with fresh context and return only a summary to the parent | agent-loop · "Keep context efficient" |
| 13 | `allowed_tools` auto-approves; `disallowed_tools` blocks; `permission_mode` covers the rest | agent-loop · "Tool permissions" |
| 14 | Permission modes: default, acceptEdits, plan, dontAsk, auto (TS only), bypassPermissions | agent-loop · "Permission mode" |
| 15 | Read-only tools run in parallel; Edit/Write/Bash run sequentially | agent-loop · "Parallel tool execution" |
| 16 | Hooks: PreToolUse, PostToolUse, UserPromptSubmit, Stop, SubagentStart/Stop, PreCompact; run outside the context window | agent-loop · "Hooks" |
| 17 | ResultMessage subtypes incl. `error_during_execution`, `error_max_structured_output_retries`; `result` only on success; all carry cost/usage/num_turns/session_id | agent-loop · "Handle the result" |
| 18 | Capture `session_id` to resume with full context; can also fork a session | agent-loop · "Sessions and continuity" |
| 19 | "Put it all together" agent (allowed_tools, setting_sources, max_turns=30, effort=high) | agent-loop · "Put it all together" |

## Not from the source (author's own practice — labeled as such on the page)

- Looping over every page in the hub repo to reformat the site (real workflow).
- Multi-step debugging loop in code review with `acceptEdits` + a `PreToolUse` repo-fence hook (real workflow).
- Specific default numbers used as examples (`max_budget_usd = 2.00`) are illustrative, not prescribed by the docs.
