from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

from simple_search.problems.wolf_goat_cabbage import WolfGoatCabbageState

@dataclass
class _Node:
    state: Any
    action: Optional[str]
    parent: Optional["_Node"]


@dataclass
class BFSStats:
    nodes_generated: int = 0
    nodes_expanded: int = 0
    max_frontier_size: int = 0
    solution_depth: Optional[int] = None
    solution_cost: Optional[float] = None


def bfs(problem, return_stats: bool = False) -> List[Tuple[Any, Optional[str]]]:
    stats = BFSStats()
    start = problem.start
    if problem.GoalTest(start):
        stats.solution_depth = 0
        stats.solution_cost = 0.0
        if return_stats:
            return ([(start, None)], stats)
        return [(start, None)]

    frontier = deque([_Node(start, None, None)])
    explored = set()
    stats.max_frontier_size = max(stats.max_frontier_size, len(frontier))

    while frontier:
        node = frontier.popleft()
        stats.nodes_expanded += 1
        explored.add(node.state)

        for action in problem.Actions(node.state):
            child_state = problem.Transition(node.state, action)
            stats.nodes_generated += 1
            if hasattr(child_state, "is_valid") and not child_state.is_valid():
                continue
            if child_state in explored:
                continue
            if any(n.state == child_state for n in frontier):
                continue
            child = _Node(child_state, action, node)
            frontier.append(child)
            stats.max_frontier_size = max(stats.max_frontier_size, len(frontier))

            if problem.GoalTest(child_state):
                path: List[Tuple[Any, Optional[str]]] = []
                cur: Optional[_Node] = child
                cost = 0.0
                while cur is not None:
                    path.append((cur.state, cur.action))
                    if cur.parent is not None:
                        try:
                            cost += problem.Cost(cur.parent.state, cur.action, cur.state)
                        except Exception:
                            cost += 1.0
                    cur = cur.parent
                path.reverse()
                stats.solution_depth = len(path) - 1
                stats.solution_cost = cost
                if return_stats:
                    return (path, stats)
                return path
    if return_stats:
        return ([], stats)
    return []
