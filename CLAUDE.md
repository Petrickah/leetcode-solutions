# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## What this repository is

Algorithmic interview-practice solutions in Python — LeetCode, HackerRank,
NeetCode, Advent of Code, and similar. One folder per problem:
`<platform>/<problem-slug>/{solution.py, notes.md}`.

## Review workflow — read before touching any problem folder

This repo has a strict division of labor:

- **The user writes the algorithm and the reasoning behind it.** Claude never
  authors or rewrites the algorithm, and never edits `solution.py` beyond the
  initial scaffold (see "Scaffolding a new problem" below).
- **When asked to review a problem**: read `notes.md` first for the problem
  statement and the user's intended approach, then read `solution.py`.
- **Feedback goes in the `## Feedback` section of `notes.md`** — correctness
  issues, complexity analysis, edge cases, style. Point at what's wrong or
  suboptimal and why; don't hand over rewritten code or step-by-step
  pseudocode that amounts to solving it for them.
- **Claude may update `notes.md` frontmatter** (`status`, `time_complexity`,
  `space_complexity`, `date`) to reflect the review outcome. The
  `## My Approach` section is the user's own reasoning — never edit it.
- The user rewrites `solution.py` based on the feedback; the cycle repeats
  until the note's `status` is set to `done`.

## Scaffolding a new problem

Claude may set up a brand-new problem folder from a raw problem statement:

- The user drops the statement (+ source URL) into a `raw.md` scratch file
  inside the problem folder, or pastes it directly into the conversation.
  `raw.md` is gitignored — it's disposable intake, never committed.
- Claude creates `solution.py` from `templates/solution_template.py`
  (empty stub — no logic, ever) and `notes.md` from
  `templates/notes_template.md`, with frontmatter filled in from what's
  knowable (`platform`, `url`, `difficulty`/`tags` if stated) and the
  `## Problem` section rewritten as a clear, condensed restatement of the
  raw text — this is copy transcribed from the source, not the user's own
  writing, so reformatting it for clarity is fine.
- `## My Approach` and `## Feedback` stay empty for the user to fill in.
- This scaffolding step never touches `solution.py`'s body beyond the
  template stub, and never writes anything resembling a solution.

## Commands

Run a solution: `python <platform>/<problem-slug>/solution.py`

No test runner yet — add one here if/when it's introduced.

## Structure

```
<platform>/<problem-slug>/
  solution.py
  notes.md
templates/
  solution_template.py
  notes_template.md
```
