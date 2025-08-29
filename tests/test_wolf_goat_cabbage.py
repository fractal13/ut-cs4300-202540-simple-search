import sys
from pathlib import Path
import itertools
import pytest

# Quick test-time fix: make src importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wolf_goat_cabbage import (
    WolfGoatCabbageState,
    WolfGoatCabbageProblem,
    CROSS_ALONE,
    TAKE_GOAT,
    TAKE_WOLF,
    TAKE_CABBAGE,
)


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
    assert CROSS_ALONE in actions
    assert TAKE_GOAT in actions

    # take goat
    s2 = prob.Transition(s, TAKE_GOAT)
    assert s2.goat != s.goat
    assert s2.farmer != s.farmer


def test_actions_comprehensive():
    prob = WolfGoatCabbageProblem()
    # define expected actions based on who's on same side as farmer
    for s in all_states():
        acts = set(prob.Actions(s))
        expected = {CROSS_ALONE}
        if s.farmer == s.wolf:
            expected.add(TAKE_WOLF)
        if s.farmer == s.goat:
            expected.add(TAKE_GOAT)
        if s.farmer == s.cabbage:
            expected.add(TAKE_CABBAGE)
        assert acts == expected, f"Actions for {s} incorrect: got {acts}, expected {expected}"


def test_transition_comprehensive():
    prob = WolfGoatCabbageProblem()
    for s in all_states():
        possible = prob.Actions(s)
        for a in possible:
            s2 = prob.Transition(s, a)
            # farmer should move
            assert s2.farmer != s.farmer, f"Farmer didn't move for action {a} on {s} -> {s2}"
            # check moved passenger if any
            if a == TAKE_WOLF:
                assert s2.wolf != s.wolf
                assert s2.goat == s.goat and s2.cabbage == s.cabbage
            elif a == TAKE_GOAT:
                assert s2.goat != s.goat
                assert s2.wolf == s.wolf and s2.cabbage == s.cabbage
            elif a == TAKE_CABBAGE:
                assert s2.cabbage != s.cabbage
                assert s2.wolf == s.wolf and s2.goat == s.goat
            elif a == CROSS_ALONE:
                assert s2.wolf == s.wolf and s2.goat == s.goat and s2.cabbage == s.cabbage
            else:
                pytest.skip(f"Unknown action {a}")


def test_goal_and_cost_pytest_style():
    prob = WolfGoatCabbageProblem()
    assert not prob.GoalTest(prob.start)
    assert prob.GoalTest(prob.goal)
    c = prob.Cost(prob.start, "cross_alone", prob.goal)
    assert c == pytest.approx(1.0)
