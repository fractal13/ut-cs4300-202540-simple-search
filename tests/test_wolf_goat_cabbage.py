import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wolf_goat_cabbage import WolfGoatCabbageState, WolfGoatCabbageProblem


def test_state_validity():
    s = WolfGoatCabbageState(True, True, True, True)
    assert s.is_valid()

    # goat with wolf without farmer -> invalid
    s2 = WolfGoatCabbageState(False, False, True, True)
    assert not s2.is_valid()

    # goat with cabbage without farmer -> invalid
    s3 = WolfGoatCabbageState(False, True, True, False)
    assert not s3.is_valid()


def test_actions_and_transition():
    prob = WolfGoatCabbageProblem()
    s = prob.start
    actions = prob.Actions(s)
    assert "cross_alone" in actions
    assert "take_goat" in actions

    # take goat
    s2 = prob.Transition(s, "take_goat")
    assert s2.goat != s.goat
    assert s2.farmer != s.farmer


def test_goal_and_cost():
    prob = WolfGoatCabbageProblem()
    assert not prob.GoalTest(prob.start)
    assert prob.GoalTest(prob.goal)
    c = prob.Cost(prob.start, "cross_alone", prob.goal)
    assert c == 1.0
