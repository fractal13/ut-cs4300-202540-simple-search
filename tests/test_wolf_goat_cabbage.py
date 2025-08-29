import sys
from pathlib import Path
import itertools
import pytest

# Quick test-time fix: make src importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wolf_goat_cabbage import WolfGoatCabbageState, WolfGoatCabbageProblem


def all_states():
    for farmer, wolf, goat, cabbage in itertools.product([False, True], repeat=4):
        yield WolfGoatCabbageState(farmer, wolf, goat, cabbage)


def test_state_validity_all_states():
    # enumerate all 16 states and check validity matches rules
    for s in all_states():
        goat_with_wolf = (s.goat == s.wolf) and (s.goat != s.farmer)
        goat_with_cabbage = (s.goat == s.cabbage) and (s.goat != s.farmer)
        expected_valid = not (goat_with_wolf or goat_with_cabbage)
        assert s.is_valid() == expected_valid, f"State {s} validity mismatch"


def test_actions_and_transition_pytest_style():
    prob = WolfGoatCabbageProblem()
    s = prob.start
    actions = prob.Actions(s)
    assert "cross_alone" in actions
    assert "take_goat" in actions

    # take goat
    s2 = prob.Transition(s, "take_goat")
    assert s2.goat != s.goat
    assert s2.farmer != s.farmer


def test_goal_and_cost_pytest_style():
    prob = WolfGoatCabbageProblem()
    assert not prob.GoalTest(prob.start)
    assert prob.GoalTest(prob.goal)
    c = prob.Cost(prob.start, "cross_alone", prob.goal)
    assert c == pytest.approx(1.0)
