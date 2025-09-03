import pytest

from simple_search.problems.eight_puzzle import (
    EightPuzzleState,
    EightPuzzleProblem,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    ZERO,
    MISPLACED,
    MANHATTAN,
)


def test_state_valid_and_tuple():
    s = EightPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0))
    assert s.as_tuple() == (1, 2, 3, 4, 5, 6, 7, 8, 0)
    assert s.is_valid()


def test_state_invalid():
    s = EightPuzzleState((1, 2, 3))
    assert not s.is_valid()


def test_actions_corners_and_center():
    s = EightPuzzleState((0, 1, 2, 3, 4, 5, 6, 7, 8))
    prob = EightPuzzleProblem(start=s)
    actions = set(prob.Actions(s))
    assert actions == {DOWN, RIGHT}

    s2 = EightPuzzleState((1, 2, 3, 4, 0, 5, 6, 7, 8))
    prob2 = EightPuzzleProblem(start=s2)
    actions2 = set(prob2.Actions(s2))
    assert actions2 == {UP, DOWN, LEFT, RIGHT}


def test_transition_swaps_tiles():
    s = EightPuzzleState((0, 1, 2, 3, 4, 5, 6, 7, 8))
    prob = EightPuzzleProblem(start=s)
    s_right = prob.Transition(s, RIGHT)
    assert isinstance(s_right, EightPuzzleState)
    assert s_right.as_tuple() == (1, 0, 2, 3, 4, 5, 6, 7, 8)

    s_down = prob.Transition(s, DOWN)
    assert s_down.as_tuple() == (3, 1, 2, 0, 4, 5, 6, 7, 8)

    with pytest.raises(ValueError):
        prob.Transition(s, "jump")


def test_goal_and_cost():
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    s_goal = EightPuzzleState(goal)
    prob = EightPuzzleProblem(start=s_goal, goal=goal)
    assert prob.GoalTest(s_goal)
    assert prob.Cost(s_goal, UP, s_goal) == 1.0


def test_heuristics_zero_misplaced_manhattan():
    s = EightPuzzleState((2, 1, 3, 4, 5, 6, 7, 8, 0))
    prob_zero = EightPuzzleProblem(start=s, heuristic=ZERO)
    prob_mis = EightPuzzleProblem(start=s, heuristic=MISPLACED)
    prob_man = EightPuzzleProblem(start=s, heuristic=MANHATTAN)

    assert prob_zero.Heuristic(s) == 0.0
    assert prob_mis.Heuristic(s) == 2.0
    assert prob_man.Heuristic(s) == 2.0


def test_fmt_state_multiline():
    s = EightPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0))
    prob = EightPuzzleProblem(start=s)
    out = prob.fmt_state(s)
    assert "\n" in out
    lines = out.splitlines()
    assert lines[0] == "1 2 3"
    assert lines[-1] == "7 8 0"
