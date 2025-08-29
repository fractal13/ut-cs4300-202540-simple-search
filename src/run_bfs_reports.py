from __future__ import annotations
from typing import List, Tuple
from wolf_goat_cabbage import (
    WolfGoatCabbageState,
    WolfGoatCabbageProblem,
    CROSS_ALONE,
    TAKE_GOAT,
    TAKE_WOLF,
    TAKE_CABBAGE,
)
from bfs import bfs

ACTION_LABELS = {
    CROSS_ALONE: "Return alone",
    TAKE_GOAT: "Move Goat",
    TAKE_WOLF: "Move Wolf",
    TAKE_CABBAGE: "Move Cabbage",
}


def fmt_state(s: WolfGoatCabbageState) -> str:
    return "(" + ",".join("L" if v else "R" for v in s.as_tuple()) + ")"


def print_report(start: WolfGoatCabbageState, goal: WolfGoatCabbageState | None = None) -> None:
    goal = goal or WolfGoatCabbageState(False, False, False, False)
    prob = WolfGoatCabbageProblem(start=start, goal=goal)
    path, stats = bfs(prob, return_stats=True)

    print(f"Domain: WGC | Algorithm: BFS")
    print(f"Solution cost: {stats.solution_cost} | Depth: {stats.solution_depth}")
    print(f"Nodes generated: {stats.nodes_generated} | Nodes expanded: {stats.nodes_expanded} | Max frontier: {stats.max_frontier_size}")
    print("Path:")
    for i, (state, action) in enumerate(path[1:], start=1):
        label = ACTION_LABELS.get(action, str(action))
        prev_state = path[i-1][0]
        print(f"  {i}) {label:15} {fmt_state(prev_state)} -> {fmt_state(state)}")
    print()


def main():
    starts = [
        WolfGoatCabbageState(True, True, True, True),
        # example other starts: farmer left, others right
        WolfGoatCabbageState(True, False, False, False),
        WolfGoatCabbageState(False, True, True, True),
    ]
    for s in starts:
        if not s.is_valid():
            print(f"Skipping invalid start state: {fmt_state(s)}")
            continue
        print_report(s)


if __name__ == "__main__":
    main()
