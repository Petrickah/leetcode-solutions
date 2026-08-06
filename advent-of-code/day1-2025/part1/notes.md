---
status: done
date: 2026-08-05
platform: advent-of-code
url: https://adventofcode.com/2025/day/1
difficulty:
tags: [simulation, modular-arithmetic]
time_complexity: O(n)
space_complexity: O(1)
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

Because the safe uses a rotative dial numbered `0.99`, each operation towards one of 
the directions is a modulo addition or substraction as follows:
- `L<n>` — rotate left (toward lower numbers) by `n` clicks - `(c - n) % 100`
- `R<n>` — rotate right (toward higher numbers) by `n` clicks - `(c + n) % 100`

The rotations are pointing at `0` when the modulo operation is equal to the expected value.

I would iterate line by line and read the first character and the rest as a number. The first
character tells which modulo operation gets applied by n clicks in that direction. The end result
keeps updating until all the operations are done. Each update checks if the result is `0` and 
increments a counter.

``` pseudocode
counter = 0
value, size = 50, 100
foreach operation in sequence:
    (o, n) = 
        (operation[0], int(operation[1:]))
    value = (o is 'L') 
        ? ((value - n) % size)
        : ((value + n) % size)
    counter = (value is 0)
        ? (counter+1)
        : (counter)
return counter
```

## Feedback

Traced the pseudocode by hand against the worked example
(`L68 L30 R48 L5 R60 L55 L1 L99 R14 L82` from 50) — it produces `3`, matching
the expected output. The core idea (dial position is a running value taken
mod 100, `L` subtracts, `R` adds, check for `0` after each update) is right.

A few things to think about before/while turning this into `solution.py`:

- **Modulo sign**: `(value - n) % size` relies on `%` always returning a
  non-negative result when the modulus is positive — true in Python, but
  *not* in C/C++/Java/JS, where `%` is truncated and can return a negative
  value for a negative left operand (e.g. `-18 % 100` is `-18` in those
  languages, not `82`). Worth keeping in mind since this is exactly the kind
  of thing that silently breaks a "correct" algorithm when ported to another
  language in an interview setting.
- **Parsing robustness**: `operation[1:]` assumes each line is already a
  clean `L<n>`/`R<n>` token. If you're reading from a file, lines will likely
  carry a trailing `\n` (and possibly trailing whitespace) — `int(operation[1:])`
  will choke on that unless each line is stripped first.
- **Complexity**: this is a single pass over the input, one constant-time
  update per line — O(n) time for n rotations, O(1) extra space beyond
  reading the input (added to frontmatter below).

No correctness issues found in the approach itself — looks solid to implement as-is.

---

**On the `with_file` decorator attempt in `solution.py`**: good instinct to
reach for a decorator, but there's a real bug and a design gap:

- **Bug — EOF crashes it.** `still_reading = not file_line is ''` is set
  *before* `func(...)` is called in the same loop iteration, so on hitting
  the empty string `readline()` returns at EOF, the loop body still runs
  `func(file_line[0], int(file_line[1:]))` on `''` — `file_line[0]` raises
  `IndexError: string index out of range`. Setting a flag mid-body doesn't
  stop the rest of that same iteration; you'd need to check-and-`break`
  before calling `func`, not after.
- **Design gap — no state across lines.** `solve(op, n_clicks)` gets called
  once per line, but `counter`, `value`, and `size` are declared *inside*
  `solve`, so they reset to fresh values on every single call — nothing
  persists between rotations. The decorator would need to either pass the
  running state in/out of each call, or (simpler) hand `solve` the whole
  input at once and let it loop internally.
- **Style nits**: `is`/`is not` is for identity, not value equality —
  `file_line is ''` is fragile (string interning isn't guaranteed); use
  `==`/`!=` or plain truthiness (`if not file_line`). `typing.Callable` is
  the idiomatic type hint for a function argument, not `types.FunctionType`.
- I pushed a corrected, more generic version to
  `templates/solution_template.py` (a `read_lines(filename="input.txt")`
  decorator that hands the whole list of lines to `solve` in one call, so
  state naturally lives in `solve`'s own scope) — figured infra/boilerplate
  like this belongs in the shared template rather than me editing your
  `solution.py` directly. Feel free to pull the pattern in and adapt it.

---

**Final `solution.py` review — ran it, output is `1139` on your `input.txt`.**
Also re-checked the algorithm against the worked example separately: `3`,
matching the puzzle text. No correctness issues.

- The state-across-lines gap from the earlier `with_file` attempt is fixed:
  `read_lines` now hands the whole `lines` list to `solve` in one call, so
  `counter`/`value` correctly persist across the loop inside `solve`'s own
  scope.
- `solve(lines, start, size)` called as `solve(start=50, size=100)` works
  cleanly with the decorator's `func(lines, *args, **kwargs)` — keyword args
  pass through fine alongside the injected `lines`.
- Minor, non-blocking: no `else` branch if a line's op char is neither `L`
  nor `R` — `value` would silently stay unchanged. Not an issue for
  well-formed AoC input, just noting it as a robustness edge case.
- The `# type: ignore` on the `solve(...)` call is because a generic
  `*args, **kwargs` decorator erases the wrapped function's signature from
  a type checker's point of view — expected with this decorator shape, not
  something wrong with your code.

Solved and correct.
