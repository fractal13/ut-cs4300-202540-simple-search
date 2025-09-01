from __future__ import annotations
from typing import Tuple
import argparse

from wolf_goat_cabbage import (
    WolfGoatCabbageState,
    WolfGoatCabbageProblem,
    CROSS_ALONE,
    TAKE_GOAT,
    TAKE_WOLF,
    TAKE_CABBAGE,
)
from bfs import bfs
from ids import ids

ACTION_LABELS = {
    CROSS_ALONE: "Return alone",
    TAKE_GOAT: "Move Goat",
    TAKE_WOLF: "Move Wolf",
    TAKE_CABBAGE: "Move Cabbage",
}


def parse_start(s: str) -> WolfGoatCabbageState:
    s = s.strip().upper()
    if len(s) != 4 or any(ch not in ("L", "R") for ch in s):
        raise argparse.ArgumentTypeError("start must be 4 characters long using only L or R, e.g. LLLL")
    # map 'L'->True (left) as used in existing scripts where True meant left
    vals = tuple(ch == "L" for ch in s)
    return WolfGoatCabbageState(*vals)


def fmt_state(s: WolfGoatCabbageState) -> str:
    return "(" + ",".join("L" if v else "R" for v in s.as_tuple()) + ")"


def print_report(start: WolfGoatCabbageState, algo: str, goal: WolfGoatCabbageState | None = None) -> None:
    goal = goal or WolfGoatCabbageState(False, False, False, False)
    prob = WolfGoatCabbageProblem(start=start, goal=goal)
    if algo == "bfs":
        path, stats = bfs(prob, return_stats=True)
        alg_label = "BFS"
    else:
        path, stats = ids(prob, return_stats=True)
        alg_label = "IDS"

    print(f"Domain: WGC | Algorithm: {alg_label}")
    print(f"Solution cost: {stats.solution_cost} | Depth: {stats.solution_depth}")
    print(f"Nodes generated: {stats.nodes_generated} | Nodes expanded: {stats.nodes_expanded} | Max frontier: {stats.max_frontier_size}")
    print("Path:")
    for i, (state, action) in enumerate(path[1:], start=1):
        label = ACTION_LABELS.get(action, str(action))
        prev_state = path[i - 1][0]
        print(f"  {i}) {label:15} {fmt_state(prev_state)} -> {fmt_state(state)}")
    print()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="run_reports.py", description="Run WGC reports with BFS or IDS")
    sub = parser.add_subparsers(dest="algo", required=True, help="algorithm to run")

    p_bfs = sub.add_parser("bfs", help="Run BFS on example starts or a provided start")
    p_bfs.add_argument("--start", type=parse_start, default=None, help="Start state as 4 chars L/R (farmer,wolf,goat,cabbage). Default: runs examples")

    p_ids = sub.add_parser("ids", help="Run IDS on example starts or a provided start")
    p_ids.add_argument("--start", type=parse_start, default=None, help="Start state as 4 chars L/R (farmer,wolf,goat,cabbage). Default: runs examples")

    args = parser.parse_args(argv)

    # example starts from original scripts
    example_starts = [
        WolfGoatCabbageState(True, True, True, True),
        WolfGoatCabbageState(False, False, False, True),
        WolfGoatCabbageState(False, True, False, True),
    ]

    if args.start is not None:
        s = args.start
        if not s.is_valid():
            print(f"Invalid start state: {fmt_state(s)}")
            return
        print_report(s, args.algo)
    else:
        for s in example_starts:
            if not s.is_valid():
                print(f"Skipping invalid start state: {fmt_state(s)}")
                continue
            print_report(s, args.algo)


if __name__ == "__main__":
    main()
