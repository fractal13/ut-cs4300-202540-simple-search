# Water Jug (Water Pouring) Puzzle - Problem Description

## Problem statement
- Given N jugs with capacities C = [c1, c2, ..., cN], an initial volume vector V0 (commonly all zeros), and a target volume T, find a sequence of actions (fill, empty, pour) that results in at least one jug containing volume T, or determine that no solution exists.

## State representation
- State: tuple V = (v1, v2, ..., vN) with 0 <= vi <= ci for each jug i.
- Represent states as immutable tuples of ints for hashing and membership tests.

## Initial state
- Default: V0 = (0, 0, ..., 0).
- Allow arbitrary initial vectors as input.

## Actions
- `fill(i)`: fill jug i from an external source so vi := ci.
- `empty(i)`: empty jug i to waste so vi := 0.
- `pour(i, j)`: transfer := min(vi, cj - vj); vi := vi - transfer; vj := vj + transfer.

## Transition
- Transitions are deterministic and atomic; applying an action to state V produces a single successor state defined by the action semantics.
- From a state V, valid successor actions exclude no-ops (e.g., filling an already full jug or emptying an already empty jug).
- The successor set size per state is up to N fills + N empties + N*(N-1) pours, but practical pruning reduces this.

## GoalTest
- GoalTest(state): returns True iff there exists an index i with state[i] == T.
- The goal is satisfied by any jug equaling T; no other goal variants are allowed.

## Cost
- Default cost model: uniform-cost per action (each action has cost 1).
- Optional cost models:
  - amount-based: cost(action) = amount transferred (for pour) or capacity for fill/empty.

## Example instances
- Two-jug classic: `capacities=[3,5]`, `initial=[0,0]`, `target=4` -> expected solution using pours and fills.
- Three-jug example: `capacities=[8,5,3]`, target e.g., `4` in any jug.
- Unsolvable example: `capacities=[2,4]`, `target=3`.
