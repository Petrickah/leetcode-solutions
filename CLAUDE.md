# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## What this repository is

Algorithmic interview-practice solutions in Python — LeetCode, HackerRank,
NeetCode, Advent of Code, and similar. One folder per problem:
`<platform>/<problem-slug>/{solution.py, notes.md}`.

## Review workflow — read before touching any problem folder

This repo has a strict division of labor:

- **The user writes `solution.py` and `notes.md`.** Claude never authors or
  rewrites the algorithm, and never edits `solution.py`.
- **When asked to review a problem**: read `notes.md` first for the problem
  statement and the user's intended approach, then read `solution.py`.
- **Feedback goes in the `## Feedback` section of `notes.md`** — correctness
  issues, complexity analysis, edge cases, style. Point at what's wrong or
  suboptimal and why; don't hand over rewritten code or step-by-step
  pseudocode that amounts to solving it for them.
- **Claude may update `notes.md` frontmatter** (`status`, `time_complexity`,
  `space_complexity`, `date`) to reflect the review outcome. The `## Problem`
  and `## My Approach` sections are the user's own writing — never edit
  those.
- The user rewrites `solution.py` based on the feedback; the cycle repeats
  until the note's `status` is set to `done`.

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
