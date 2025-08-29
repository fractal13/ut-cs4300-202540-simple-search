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
