from __future__ import annotations
from simple_search.problems.water_jugs import WaterJugsState, WaterJugsProblem, FILL, EMPTY, POUR


def test_state_validity():
    caps = (5, 3)
    s = WaterJugsState((0, 0))
    assert s.is_valid(caps)
    s2 = WaterJugsState((5, 3))
    assert s2.is_valid(caps)
    s3 = WaterJugsState((6, 0))
    assert not s3.is_valid(caps)


def test_actions_and_transition_fill_empty_pour():
    caps = (5, 3)
    prob = WaterJugsProblem(caps, target=4)
    s0 = prob.start
    actions = prob.Actions(s0)
    # from empty state, only fills are possible
    assert (FILL, 0) in actions and (FILL, 1) in actions

    # fill jug 0
    s1 = prob.Transition(s0, (FILL, 0))
    assert s1.volumes == (5, 0)

    # pour from jug0 to jug1
    a_pour = (POUR, 0, 1)
    assert a_pour in prob.Actions(s1)
    s2 = prob.Transition(s1, a_pour)
    # jug1 capacity is 3, so transfer 3
    assert s2.volumes == (2, 3)

    # empty jug1
    s3 = prob.Transition(s2, (EMPTY, 1))
    assert s3.volumes == (2, 0)


def test_goal_test_reaches_target():
    caps = (3, 5)
    prob = WaterJugsProblem(caps, target=4)
    s = WaterJugsState((0, 5))
    assert not prob.GoalTest(s)
    s2 = WaterJugsState((4, 1))
    assert prob.GoalTest(s2)


def test_cost_models():
    caps = (5, 3)
    prob = WaterJugsProblem(caps, target=4)
    s0 = WaterJugsState((5, 0))
    s1 = prob.Transition(s0, (POUR, 0, 1))
    # amount poured should be 3
    cost = prob.Cost(s0, (POUR, 0, 1), s1)
    assert cost == 3.0
    # fill cost
    s_fill = prob.Transition(s0, (EMPTY, 0))
    assert prob.Cost(s0, (EMPTY, 0), s_fill) == 1.0
