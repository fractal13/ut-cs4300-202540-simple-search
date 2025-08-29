import sys
from pathlib import Path

# make src importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from wolf_goat_cabbage import WolfGoatCabbageState, WolfGoatCabbageProblem, CROSS_ALONE
from bfs import bfs


def test_bfs_goal_start():
    goal = WolfGoatCabbageState(False, False, False, False)
    prob = WolfGoatCabbageProblem(start=goal, goal=goal)
    path = bfs(prob)
    assert path == [(goal, None)]


def test_bfs_one_step_from_goal():
    goal = WolfGoatCabbageState(False, False, False, False)
    # generate states one action away from goal by reversing transitions
    prob = WolfGoatCabbageProblem(goal=goal)
    one_step_states = []
    for s_bits in __import__('itertools').product([False, True], repeat=4):
        s = WolfGoatCabbageState(*s_bits)
        for a in prob.Actions(s):
            if prob.Transition(s, a) == goal:
                one_step_states.append((s, a))
    assert len(one_step_states) > 0
    # test BFS returns path of length 2 (start->goal) for each such state
    for s, a in one_step_states:
        prob2 = WolfGoatCabbageProblem(start=s, goal=goal)
        path = bfs(prob2)
        assert len(path) == 2
        assert path[0][0] == s and path[0][1] is None
        assert path[1][0] == goal and path[1][1] == a
