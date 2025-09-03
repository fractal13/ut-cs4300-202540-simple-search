Problem: 8-puzzle (sliding tile puzzle)

Performance measure
- Primary: minimal number of moves to reach the goal
- Secondary: time to solution, memory used (nodes expanded / frontier size), solution optimality (compared to known optimal)
- Tertiary: robustness (handles invalid/unsolvable inputs), reproducibility

Environment
- Deterministic: moves have deterministic outcome
- Fully observable: the entire board configuration is known
- Discrete: finite board positions (3x3 grid with tiles 1..8 and blank)
- Static during agent decision (only changes due to agent actions)
- Single-agent problem
- Episodic vs Sequential: sequential — the agent's actions affect future decisions and the episode consists of a sequence of moves from start to goal (not independent episodes)

Actuators
- Slide a tile into the blank space in one of up/down/left/right directions (when legal)
- Actions are atomic and instantaneous in the model

Sensors
- Read the full board configuration (tile positions)
- Detect whether current state equals goal

Notes
- Some start states are unsolvable; agent should detect or handle unsolvable instances
- Representations: state can be a tuple of length 9, 3x3 list, or matrix; actions encoded as move directions or tile indices
- Cost model: uniform step cost (1 per slide) for classic shortest-path; alternative cost models may weight moves
