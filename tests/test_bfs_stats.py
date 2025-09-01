import sys
from pathlib import Path

from simple_search.problems.wolf_goat_cabbage import WolfGoatCabbageState, WolfGoatCabbageProblem
from simple_search.search.bfs import bfs, BFSStats


def test_bfs_stats_goal_start():
    goal = WolfGoatCabbageState(False, False, False, False)
    prob = WolfGoatCabbageProblem(start=goal, goal=goal)
    path, stats = bfs(prob, return_stats=True)
    assert path == [(goal, None)]
    assert isinstance(stats, BFSStats)
    assert stats.solution_depth == 0
    assert stats.solution_cost == 0.0


def test_bfs_stats_standard_start():
    start = WolfGoatCabbageState(True, True, True, True)
    goal = WolfGoatCabbageState(False, False, False, False)
    prob = WolfGoatCabbageProblem(start=start, goal=goal)
    path, stats = bfs(prob, return_stats=True)
    assert path
    assert isinstance(stats, BFSStats)
    # nodes generated/expanded should be positive
    assert stats.nodes_generated > 0
    assert stats.nodes_expanded > 0
    assert stats.max_frontier_size > 0
    assert stats.solution_depth == len(path) - 1
    assert stats.solution_cost is not None
