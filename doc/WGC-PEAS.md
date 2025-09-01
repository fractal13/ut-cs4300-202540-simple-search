# Wolf-Goat-Cabbage (WGC) — PEAS Analysis

This document provides a concise PEAS (Performance measure, Environment, Actuators, Sensors) assessment for the classic Wolf-Goat-Cabbage puzzle as implemented in this repository.

## Task description
A farmer must transport a wolf, a goat, and a cabbage across a river using a boat that can carry the farmer and at most one item. If left alone together without the farmer, the wolf will eat the goat, and the goat will eat the cabbage. The goal is to move all items safely to the far bank.

## Performance measure
- Success: all three items and the farmer end on the goal bank.
- Safety: avoid any state in which an item is eaten (wolf with goat alone, goat with cabbage alone).
- Efficiency: minimize number of crossings (steps) required to achieve success.
- Robustness: handle invalid actions gracefully and avoid repeated unnecessary moves.

## Environment
- Deterministic: actions have predictable outcomes.
- Fully observable: the positions of farmer, wolf, goat, and cabbage are known at all times.
- Discrete and finite: state space consists of positions (left/right) for four entities; there are 16 possible configurations, fewer when invalid (eaten) states are excluded.
- Episodic: solved when goal state reached; episodes end on success or unsafe state.
- Static: environment does not change except through agent actions.
- Single-agent: the farmer (agent) controls all actions.

## Actuators
- Move alone: farmer crosses alone to the other bank.
- Move with item: farmer crosses with one of {wolf, goat, cabbage}.
- Each action toggles the bank of the farmer and optionally one item; actions are constrained by boat capacity and safety rules.

## Sensors
- State observation: current bank (left/right) of farmer, wolf, goat, cabbage.
- Validity check: ability to detect whether an observed configuration is safe (no predator-prey pair left alone).

## Discussion / Notes
- Search formulation: suitable for state-space search algorithms (BFS for optimal steps, IDS/DFS for memory-efficient exploration).
- In this repo: the WGC problem is modeled as a small, explicit state-space with safety constraints and is useful for testing search implementations and performance metrics.

