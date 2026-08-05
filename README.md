# LeetCode Solutions

## Overview

Personal collection of algorithm and data-structure solutions for coding-interview
practice — problems from LeetCode, HackerRank, NeetCode, Advent of Code, and similar
sources. Every problem gets its own folder with a Python solution and an
Obsidian-style Markdown note documenting the problem and the approach.

## Structure

```
<platform>/<problem-slug>/
  solution.py
  notes.md
```

Platform folders are lowercase: `leetcode/`, `hackerrank/`, `neetcode/`,
`aoc/<year>/day<NN>/`, etc.

Templates for a new problem live in [templates/](templates/): copy
`templates/solution_template.py` and `templates/notes_template.md` into the new
problem folder.

## Setup

Python 3.x, standard library only unless a specific problem needs a package —
any such dependency is noted in that problem's `notes.md`.

## Usage

Run a solution directly:

```
python <platform>/<problem-slug>/solution.py
```

## Workflow

1. **New problem**: I drop the raw problem statement (+ URL) into a `raw.md`
   scratch file in the problem folder (gitignored, disposable), or paste it
   into the conversation. Claude scaffolds `solution.py` (empty template
   stub) and `notes.md` (frontmatter filled in, `## Problem` condensed from
   the raw text).
2. I write the algorithm in `solution.py` and my reasoning in `notes.md`'s
   `## My Approach` section.
3. Claude reviews both files and adds feedback under the `## Feedback`
   section of `notes.md` (correctness, complexity, edge cases, style) and
   updates the note's frontmatter (status, complexity, date). Claude never
   writes or rewrites the algorithm.
4. I revise `solution.py` myself based on the feedback. Repeat until
   `status: done`.
