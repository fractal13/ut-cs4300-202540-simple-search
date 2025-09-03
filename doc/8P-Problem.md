8-Puzzle problem specification

State
- Representation: a length-9 tuple of integers (0..8) in row-major order representing the 3x3 board; 0 denotes the blank.
- Example: (1,2,3,4,5,6,7,8,0) is the goal state.
- Methods required on state objects:
  - as_tuple() -> Tuple[int, ...]: return canonical immutable tuple for hashing/comparison
  - is_valid() -> bool: optional; may verify tile set contains exactly 0..8

Initial states
- Any permutation of (0..8) that is reachable (solvable). Start state is provided by the user; default can be the goal state or a standard scrambled configuration.

Actions
- Action set: moves that slide an adjacent tile into the blank. Encode actions as one of the strings: 'up', 'down', 'left', 'right' meaning move the blank in that direction (equivalently slide the tile into the blank).
- Legal action criteria: the blank's row/column must permit the move (e.g., cannot move up when blank is in top row).
- Actions(state) -> List[str]: return only legal moves from the given state.

Transition
- Transition(s, a) -> s': perform the slide corresponding to action a and return a new State with tiles swapped.
- Implementation notes: compute blank index i (0..8) and target index j based on action; swap entries at i and j to create new tuple.

GoalTest
- GoalTest(s) -> bool: returns True when state's tuple equals goal tuple (default (1,2,3,4,5,6,7,8,0)).

Cost
- Cost(s, a, s') -> float: default uniform step cost 1.0 per move.

Heuristic
- Heuristic(s) -> float: admissible heuristic for A*/informed search; include at least three common options:
  - h_zero: the trivial zero heuristic (returns 0 for all states); equivalent to uninformed A* (i.e., Dijkstra).
  - h_misplaced: number of tiles not in goal position (excluding blank).
  - h_manhattan: sum of Manhattan distances of tiles from their goal positions (excluding blank). This is the recommended default admissible heuristic.
- Provide formula and implementation notes: to compute Manhattan, map tile value v to goal index (v-1) except blank (0 -> goal index 8). For tile at index i, row=i//3, col=i%3; goal row/col similarly; distance = abs(row-row_g)+abs(col-col_g).

Other notes
- Unsolvable states: some permutations are unreachable. The project will not perform a parity solvability check; instead, graph search algorithms should be able to exhaust the reachable state space and terminate if no solution is found.
- Recommended APIs for Problem class:
  - __init__(self, start: State, goal: Tuple[int,...] = (1,2,3,4,5,6,7,8,0), heuristic: str = 'manhattan')
  - Actions(self, s: State) -> List[str]
  - Transition(self, s: State, a: str) -> State
  - GoalTest(self, s: State) -> bool
  - Cost(self, s1: State, a: str, s2: State) -> float
  - Heuristic(self, s: State) -> float
  - fmt_state(self, s: State) -> str

- Keep state objects immutable (dataclass(frozen=True) or use plain tuples) so they can be used in sets/dicts.
