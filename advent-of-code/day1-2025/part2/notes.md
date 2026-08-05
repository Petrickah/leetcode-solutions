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

**Advent of Code 2025, Day 1 — Part Two ("Secret Entrance")**

Direct continuation of [Part One](../notes.md): same dial (`0..99`), same
starting position (**50**), same list of `L<n>`/`R<n>` rotations as input.

**What changes**: the password is no longer "how many times the dial lands
on `0` *after* a rotation" — it's now every time the dial *passes through or
lands on* `0` at any point *during* a rotation, counting each such crossing
individually.

**Caution from the puzzle text**: a single large rotation can cross `0`
multiple times — e.g. a rotation of `R1000` from `50` would cross `0` ten
times before the rotation finishes. So each rotation needs to account for
however many times it wraps around the dial, not just whether its final
resting position is `0`.

**Worked example** — same rotations as Part One
(`L68 L30 R48 L5 R60 L55 L1 L99 R14 L82` from 50): the 3 end-of-rotation
zeros from Part One, plus 3 more mid-rotation crossings (during `L68`,
`R60`, and `L82`) → password `6`.

## My Approach

To compute each number of `0` during one rotation, I would need to keep the 
same solution as before but introduce one special instruction that does this.

The result is `active_rotations + final_rotations`, where `active_rotations` is
how many `0` are in one operation and `final_rotations` is how many operations
lead to `0`.

For `active_rotations` is given by: 
- the formula is: `(c + n) / 100` regardless of the operation
- but minus `1` if lands on `0`

Example: 
```
R1000
(50 + 1000) % 100 = 1050 % 100 = 50 => `new_position`
(50 + 1000) / 100 = 1050 / 100 = 10 => `active_rotations`

L68
(50 - 68) % 100 = (-18) % 100 = 82
(50 + 68) / 100 = 118 / 100 = 1

Edge Case
L5 from 0 with trace:
( 0 - 1) % 100 = (-1) % 100 = 99
(99 - 1) % 100 =  98
(98 - 1) % 100 =  97
(97 - 1) % 100 =  96
(96 - 1) % 100 =  95
Formula: (0 - 5) % 100 = (-5) % 100 = 95
```

So if we reach `0` and we have multiple `0` is one cycle
then we subtract `1` from `active_rotations`

```
R1050
(50 + 1050) % 100 = 1100 % 100 = 0
(50 + 1050) / 100 = 1100 / 100 = 11 then subtract 1 => 10
```

```
size: 5
start: 2

L15
1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2

(2 - 15) % 5 = (-13) % 5 = 5 - 3 = 2
abs(2 - 15) / 5 = abs(-13) / 5 = 13 / 5 = 2 but ends on non-zero so we add 1?
```

```
L68

49, 48, 47, ..., 3, 2, 1, 0, 99, 98, ...

(50 - 68) % 100 = (-18) % 100 = 100 - 18 = 82
(68 - 50) / 100 = (+18) / 100 = 0

if n > c then we add 1 to the active_counter?
```

## Feedback

Traced this by hand through all 10 operations of the worked example, computing
`active_rotations` (mid-rotation crossings, excluding the final click) and
`final_rotations` (final position == 0) separately per operation. With
correct per-operation counts, the sum does come out to `6`, and the three
operations with a mid-rotation crossing line up exactly with what the puzzle
text calls out (`L68`, `R60`, `L82`) — so the overall decomposition
(`active_rotations + final_rotations`, "during" excluding the final click so
it doesn't double-count with `final_rotations`) is the right idea.

**Bug in the `L` formula.** `(c - n) / 100` doesn't work — try it on `L68`
from `c=50` (the very first operation): `(50 - 68) / 100 = -18 / 100`, which
floors to a negative number. A crossing count can never be negative, and the
puzzle text itself says this rotation crosses `0` once. Compare with your own
`R` formula, `(c + n) / 100` — for `L` you need the dial to still be moving
toward *decreasing* numbers, but the arithmetic has to reflect "how far past
a multiple of 100 does this rotation reach," not `c - n` directly. Worth
re-deriving this one on paper the way you did for the `R1000` example.

**Edge case to test explicitly**: what does your `L` formula produce when
the rotation *starts* exactly at position `0`? (This happens for real in the
example — position is `0` after `R48`, then `L5` runs next.) A formula
that's tuned to work when `c` is strictly between 1 and 99 can easily be off
by one when `c == 0`, since there's no "current position" to subtract past.
Trace `L5` from `c=0` by hand (click by click, not via the formula) and
check your formula agrees.

**Also worth pinning down**: does your `active_rotations` for a given
operation include the final click, or only the clicks strictly before it? It
needs to exclude the final click — otherwise operations that already land on
`0` (like `R48`, `L55`, `L99` here) get counted twice, once in
`active_rotations` and once in `final_rotations`.

No issues with the `R` formula or the overall structure — just the `L` case
and the `c == 0` edge case to work through.

---

**Round 2 — on the unified `(c + n) / 100` formula "regardless of the
operation", minus 1 if it lands on 0.**

The "subtract 1 if it lands on `0`" rule is solid — verified it against both
`R1000` (no subtraction, `10`) and `R1050` (lands on `0`, `11 - 1 = 10`), and
both check out against a hand trace. Good instinct catching that.

The formula itself doesn't generalize to `L`, though, and the worked example
is hiding it. I ran `(c + n) / 100` across all 10 operations and the *sum*
does land on `6` — but check the per-operation values against a hand trace,
not just the total:

- **`L30` from `c = 82`** (operation 2): clicking left 30 times goes
  `81, 80, ..., 52` — never touches `0`. True crossing count is `0`. The
  formula gives `floor((82 + 30) / 100) = 1`.
- **`L82` from `c = 14`** (operation 10, the last one): the puzzle text
  itself says this rotation crosses `0` once. The formula gives
  `floor((14 + 82) / 100) = 0`.

So operation 2 overcounts by 1 and operation 10 undercounts by 1 — they
cancel out in the *sum*, which is exactly why the final answer still came
out to `6` even though two of the individual operation counts are wrong.
That's a coincidence of this particular input, not evidence the formula is
right; nothing guarantees errors cancel out on the real puzzle input (or on
Part One's larger `L`/`R` mix in general). Worth checking each operation's
value individually against a trace rather than only checking whether the
final sum matches — same lesson as the `R1000`/`R1050` checks you already
did, just applied to more than one `L` case.

Also, small arithmetic slip worth a second look: in the `L68` example,
`(50 - 68) % 100` is written as `18` — by the same rule we covered for Part
One (Python's `%` is always non-negative for a positive modulus), `-18 % 100`
is `82`, not `18`.

---

**Round 3 — on the `solution.py` implementation.**

Tried to run it against `input.txt` — it crashes:

```
FileNotFoundError: [Errno 2] No such file or directory:
'.../day1-2025/part2/input.txt'
```

`@read_lines()` defaults to `filename="input.txt"`, which the decorator
looks for next to `solution.py` — i.e. inside `part2/`. But `input.txt`
lives one level up, in `day1-2025/`, shared with Part One. The scaffold
originally passed `@read_lines("../input.txt")` for exactly this reason;
somewhere along the way it got edited back to the default. Not touching
`solution.py` myself per our workflow, but you'll need either
`@read_lines("../input.txt")` or a copy of `input.txt` inside `part2/`
before this can run.

Separately: `active_counter += (value + n_clicks) // size` (using `value`
*before* it's updated for this line, i.e. `c`) is a direct implementation of
the unified `(c + n) / 100` formula from Round 2 — same formula, same
"subtract 1 on landing at 0" rule, just in code now. That means the Round 2
counterexamples apply here too, and you don't actually need the real AoC
site to see them — they're already inside the given example:

- Operation 2 (`L30` from `c = 82`) will make `active_counter` count a
  crossing that doesn't happen (true count is `0`, the code adds `1`).
- Operation 10 (`L82` from `c = 14`) will miss a crossing that does happen
  (true count is `1`, the code adds `0`).

If you swap `input.txt` for the 10-line example from the puzzle text
temporarily and print `active_counter` after each line (not just the final
total), you should see those two operations disagree with a hand trace, even
though the final sum still comes out to `6`. That's a more direct check than
waiting on the real site, since — as found in Round 2 — the errors happen to
cancel out over this particular example, so testing only the aggregate
result won't reveal it. Testing against your actual `input.txt` might also
just come back wrong on the site, but if it happens to come back right,
that likely means the errors cancelled out again rather than that the
formula's correct — worth keeping in mind either way.

---

**Round 4 — moving the `active_counter` update to after `value` is
reassigned.**

This does change the result, and not for the better. Ran your exact `solve`
logic against the 10-line worked example (via `solve.__wrapped__(...)` to
skip the file read) instead of guessing by hand:

```
L68 => Active Counter: 1
L30 => Active Counter: 1
R48 => Active Counter: 0
L5 => Active Counter: 1
R60 => Active Counter: 2
L55 => Active Counter: 1
L1 => Active Counter: 2
L99 => Active Counter: 1
R14 => Active Counter: 1
L82 => Active Counter: 2
Example result (expected 6): 5
```

`5`, not `6` — so this version now fails even the check that the earlier
(buggy-but-coincidentally-summing-right) version passed. On the real
`input.txt` it currently prints `6406`, but that number isn't worth trusting
since the known example already disagrees.

**Why the reorder matters**: before, `(value + n_clicks) // size` used
`value` as the position *before* this rotation (call it `c`) — a quantity
that, for `R`, isn't yet reduced back into `0..99`, so dividing it by `size`
still carries information about how far the rotation overshoots a multiple
of 100. After the reorder, `value` is the position *after* rotating — which
`% size` has already folded back into `0..99`. Once it's folded back like
that, `(value + n_clicks) // size` is a different, smaller quantity that no
longer tracks the same thing; the overshoot information the division needs
was in the *un-reduced* position, and that's gone by the time `value` is
reassigned.

So: the earlier ordering (compute the crossing count from the position
*before* updating it) was structurally the right instinct, even though the
formula itself still needs the `L`-direction fix from Rounds 2–3. This
reorder is a step backward — worth reverting the ordering and focusing back
on the `L`/`R` formula distinction instead.

---

**Round 5 — current `abs(active_value ± n_clicks) // size` version.**

Ordering is back to computing from the pre-rotation position, which is
good. Ran it against the worked example (via `solve.__wrapped__(...)`,
accumulated counter printed after every line):

```
L68 => Active Counter: 0
L30 => Active Counter: 0
R48 => Active Counter: 0
L5  => Active Counter: 0
R60 => Active Counter: 1
L55 => Active Counter: 0
L1  => Active Counter: 0
L99 => Active Counter: -1
R14 => Active Counter: -1
L82 => Active Counter: -1
Example result (expected 6): 2
```

`2`, not `6`. Worth noticing on its own: `active_counter` goes **negative**
after `L99` and stays there. That alone is proof something's wrong,
independent of the final total — a count of how many times the dial crosses
`0` can never be less than zero, so the moment a trace shows a negative
value, that operation is where to look first.

Concretely, `L99` (`c = 99`, lands exactly on `0`): `abs(99 - 99) // 100 = 0`,
then the "lands on `0`" branch subtracts `1` → net `-1`. Same thing happened
back in Round 1 with `L55`/`L99` for the original `(c - n)` formula — landing
exactly on `0` needs the pre-adjustment value to be `1` (the click landing on
`0` is itself one crossing, later excluded via the `-1`), not `0`. `abs`
collapses the sign, but the *magnitude* still needs to reflect that a
same-magnitude rotation reaching a multiple of 100 is exactly one crossing —
`abs(c - n) // size` gives `0` here since `|99 - 99| = 0`, same issue as the
`L68`/`L82` cases flagged in the hints above (whenever `|c - n| < size`, this
formula gives `0`, which is very often wrong for `L`).

---

**Round 6 — the `L` formula, explained (with an authorized exception: the
final fix below was written by Claude, not the user; see note at the end).**

**Why every earlier `L` attempt was structurally off**: they all reused
`R`'s shape (`(c ± n) / size`, with `abs()` or sign flips bolted on). But
`R` and `L` aren't mirror images of the same quantity — they measure
different things relative to `c`.

- For `R`, `c` is *how far you've already traveled* past the last zero,
  moving in the increasing direction. So `(c + n) // size` directly counts
  how many full `size`-length segments the interval `[c, c+n]` covers.
- For `L`, the relevant quantity is *how far until the next zero*, moving
  in the decreasing direction — and that's not `c` reused, it's a genuinely
  different number: from position `c`, moving left, you reach `0` after
  exactly `c` clicks (`c=5` → `4,3,2,1,0`, five clicks). If `c == 0`, you
  need a full lap: `size` clicks, not `0`.

So the first zero-crossing happens at click number:
```
first_encounter = c if c > 0 else size
```
If `n < first_encounter`, the rotation never reaches `0` at all — `0`
crossings. Otherwise, one crossing at `first_encounter`, then one more
every `size` clicks after that:
```
count = (n - first_encounter) // size + 1
```
This is a "total including the final click" count, exactly like `R`'s — so
it plugs into the *same* shared "subtract 1 if the rotation lands exactly
on `0`" rule already used for `R`, no `L`-specific adjustment needed beyond
this.

Verified this by hand against every `L` operation in the worked example
(`L68`, `L30`, `L5`, `L55`, `L1`, `L99`, `L82`) before touching any code —
all seven check out, including the three persistent counterexamples from
Rounds 1–3 (`L30` from `c=82` → correctly `0`; `L5`/`L1` from `c=0` →
correctly `0`).

**On `solution.py`**: the code already had the right shape —
`first_encounter = active_value if active_value > 0 else size` and
`if n_clicks >= first_encounter:` were both correct. But the line inside:
```python
active_counter += abs(active_value - n_clicks // size)
```
had several issues at once: operator precedence makes this
`abs(active_value - (n_clicks // size))`, not
`(n_clicks - first_encounter) // size` — a completely different
expression; it used `active_value` instead of `first_encounter` (so it
would've been wrong even with correct parens, since it throws away exactly
the `c == 0` handling `first_encounter` exists for); and the `+ 1` was
missing entirely. Ran it as-is: `220` on the worked example (expected `6`).

**This one was fixed directly in `solution.py`, at the user's explicit
request, as a one-time exception** — not a change to the project's
standing review-only rule. Fixed line:
```python
active_counter += (n_clicks - first_encounter) // size + 1
```
Verified against the worked example (all 10 operations match a hand
trace, total `6`) before applying, then confirmed the full file runs
against `input.txt`: `Solution: 6684`.
