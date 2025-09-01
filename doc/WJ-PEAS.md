## PEAS for Water Jug (Water Pouring) Puzzle

### Performance measure
- Primary: reach a goal state where one or more jugs contain the specified target volume(s).
- Secondary:
  - Minimize number of actions (plan length).
  - Minimize water used from the source.
  - Minimize water wasted (emptied to sink).
  - Minimize total poured volume or execution time.
  - Robustness: correctly report unsolvable goals.
- Other metrics for reporting:
  - Nodes expanded, nodes generated, maximum frontier size, memory usage, runtime.

### Environment
- Observable: fully observable — agent perceives exact volumes of all jugs.
- Determinism: deterministic — actions have predictable outcomes.
- Episodic/Sequential: episodic — each episode is a sequence of actions toward a goal.
- Dynamics: static — no exogenous events alter the environment during an episode.
- Number of agents: single-agent.
- State-space: discrete and finite — states are integer volume vectors bounded by capacities.

### Actuators (available actions)
- `fill(i)`: fill jug i from an infinite source to capacity.
- `empty(i)`: empty jug i to waste.
- `pour(i, j)`: pour from jug i to jug j until i empty or j full (transfer = min(vi, cj - vj)).

### Sensors
- `read_volumes()`: returns current integer volumes for all jugs.
- `observe_goal_status()`: evaluates whether goal predicate holds.

### Assumptions / Domain constraints
- Volumes and capacities are integers (units of liters).
- Infinite external source and sink.
- No leaks or measurement error.
- Actions are atomic and deterministic.
