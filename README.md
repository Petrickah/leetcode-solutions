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

1. I write `solution.py` and `notes.md` for a problem — the note documents the
   problem statement and my intended approach before/while I code it.
2. Claude reviews both files and adds feedback under the `## Feedback` section
   of `notes.md` (correctness, complexity, edge cases, style) and fills in the
   note's frontmatter (status, complexity, date). Claude does not write or
   rewrite the algorithm.
3. I revise `solution.py` myself based on the feedback.
