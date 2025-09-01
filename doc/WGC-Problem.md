# Wolf-Goat-Cabbage (WGC) — Problem Description

This document describes the problem formulation used for the Wolf-Goat-Cabbage puzzle: the representation of states, available actions, state transitions, goal test, and cost function.

## State representation
A state captures the bank location (left or right) of four entities: the farmer, the wolf, the goat, and the cabbage. Representations commonly used:

- Tuple form: (farmer, wolf, goat, cabbage)
  - Each entry is one of {L, R} (or 0/1, False/True) indicating the bank.
  - Example initial state: (L, L, L, L) — all on the left bank.

- Named structure / dataclass: fields for farmer, wolf, goat, cabbage each storing a bank value.

Unsafe states (where something is eaten) are considered invalid and excluded from the state space. Specifically:
- If farmer is not with wolf and goat are on the same bank without farmer, the wolf eats the goat (invalid).
- If farmer is not with goat and goat and cabbage are on the same bank without farmer, the goat eats the cabbage (invalid).

## Initial state
- By convention the initial state is all entities on the starting bank (left): (L, L, L, L).
- The initial state must be valid (not an eaten/unsafe state). For the conventional starting configuration, it is valid.

## Actions
The agent (farmer) may perform one of the following actions at each step, subject to boat capacity and current bank restrictions:

- Cross alone: farmer moves alone to the opposite bank.
- Cross with wolf: farmer moves and takes the wolf with him/her.
- Cross with goat: farmer moves and takes the goat with him/her.
- Cross with cabbage: farmer moves and takes the cabbage with him/her.

Action preconditions:
- The farmer and any item moved must be on the same bank at the time of action.
- Boat capacity limits to the farmer and at most one item.

Actions that would result in an invalid (eaten) state are either disallowed or lead to terminal failure depending on implementation.

## Transition model
- Actions deterministically toggle the bank of the farmer and, if applicable, the chosen item.
- Applying an action to state s yields a successor state s'. After the move, check for safety:
  - If s' is unsafe (predator-prey pair alone), it is treated as invalid and typically not added to successors.
  - Otherwise s' is a legal successor.

Example: From (L, L, L, L), action Cross with goat -> (R, L, R, L).

## Goal test
- The goal is reached when all entities including the farmer are on the goal bank (right), i.e. (R, R, R, R).
- GoalTest(s) returns true iff farmer, wolf, goat, and cabbage are all on the goal bank.

## Cost function
Common choices depending on search algorithm:

- Uniform step cost: each action has cost 1. This makes BFS optimal with respect to number of crossings.

## Notes and implementation tips
- Always filter out invalid successor states during expansion to avoid exploring eaten configurations.
- Represent banks with booleans or enums for clarity and easy comparisons.
- When generating actions, only consider items located with the farmer; this reduces branching.
- For clarity in traces, record actions as "Farmer crosses alone" or "Farmer crosses with goat" with source and destination banks.

