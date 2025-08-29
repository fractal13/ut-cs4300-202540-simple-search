from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

from wolf_goat_cabbage import WolfGoatCabbageState

# Generic Problem type is duck-typed: must provide .start, Actions(s), Transition(s,a), GoalTest(s)

@dataclass
class _Node:
    state: Any
    action: Optional[str]
    parent: Optional["_Node"]


def bfs(problem) -> List[Tuple[Any, Optional[str]]]:
    """Perform breadth-first graph search on given problem.

    Returns a list of (state, action) pairs from initial state (with action None) to goal.
    If no solution found, returns an empty list.
    """
    start = problem.start
    if problem.GoalTest(start):
        return [(start, None)]

    frontier = deque([_Node(start, None, None)])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)

        for action in problem.Actions(node.state):
            child_state = problem.Transition(node.state, action)
            if child_state in explored:
                continue
            # also avoid duplicates in frontier
            if any(n.state == child_state for n in frontier):
                continue
            child = _Node(child_state, action, node)
            if problem.GoalTest(child_state):
                # reconstruct path
                path: List[Tuple[Any, Optional[str]]] = []
                cur: Optional[_Node] = child
                while cur is not None:
                    path.append((cur.state, cur.action))
                    cur = cur.parent
                path.reverse()
                return path
            frontier.append(child)
    return []
