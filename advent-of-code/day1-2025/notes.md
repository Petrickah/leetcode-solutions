---
status: draft
date:
platform: advent-of-code
url: https://adventofcode.com/2025/day/1
difficulty:
tags: [simulation, modular-arithmetic]
time_complexity:
space_complexity:
---

## Problem

**Advent of Code 2025, Day 1 — Secret Entrance**

A safe has a circular dial with clicks numbered `0..99`. It starts pointing
at **50**.

The input is a list of rotations, one per line, each in the form `L<n>` or
`R<n>`:
- `L<n>` — rotate left (toward lower numbers) by `n` clicks
- `R<n>` — rotate right (toward higher numbers) by `n` clicks

The dial wraps around: going left past `0` continues from `99`; going right
past `99` continues from `0`. (I.e. position is always `current mod 100`.)

**Goal**: apply every rotation in order, and count how many times the dial
ends up pointing at exactly `0` *after* a rotation. That count is the answer.

**Worked example** — starting at 50, applying
`L68 L30 R48 L5 R60 L55 L1 L99 R14 L82` lands on `0` three times (after
`R48`, `L55`, and `L99`), so the example answer is `3`.

## My Approach

## Feedback
