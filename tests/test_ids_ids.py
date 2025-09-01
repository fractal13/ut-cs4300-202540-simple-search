import pytest

from src.ids import ids


class ChainProblem:
    def __init__(self, start, goal, transitions, costs=None):
        self.start = start
        self._goal = goal
        self._trans = transitions
        self._costs = costs or {}

    def Actions(self, state):
        return list(self._trans.get(state, {}).keys())

    def Transition(self, state, action):
        return self._trans[state][action]

    def GoalTest(self, state):
        return state == self._goal

    def Cost(self, s1, a, s2):
        return self._costs.get((s1, a, s2), 1.0)


def path_states(path):
    return [s for s, _ in path]


def test_ids_finds_shallow_solution_quickly():
    trans = {"A": {"a": "B"}, "B": {"b": "C"}}
    p = ChainProblem(start="A", goal="B", transitions=trans)
    path = ids(p, max_limit=5, return_stats=False)
    assert path_states(path) == ["A", "B"]


def test_ids_accumulates_stats_and_finds_deep():
    # chain A->B->C->D
    trans = {"A": {"a": "B"}, "B": {"b": "C"}, "C": {"c": "D"}}
    p = ChainProblem(start="A", goal="D", transitions=trans)
    path, stats = ids(p, max_limit=5, return_stats=True)
    assert path_states(path) == ["A", "B", "C", "D"]
    assert stats.solution_depth == 3
    # IDS repeats work, so nodes_generated should be > nodes_expanded for single DLS
    assert stats.nodes_generated >= stats.nodes_expanded


def test_ids_no_solution_with_stats():
    trans = {"A": {"a": "B"}, "B": {"b": "C"}}
    p = ChainProblem(start="A", goal="Z", transitions=trans)
    path, stats = ids(p, max_limit=2, return_stats=True)
    assert path == []
    # nodes_generated should be positive
    assert stats.nodes_generated > 0
    assert stats.solution_depth is None


def test_ids_respects_max_limit():
    trans = {"A": {"a": "B"}, "B": {"b": "C"}, "C": {"c": "D"}}
    p = ChainProblem(start="A", goal="D", transitions=trans)
    # limit too small
    path = ids(p, max_limit=2, return_stats=False)
    assert path == []
    # sufficient limit
    path = ids(p, max_limit=3, return_stats=False)
    assert path != []


def test_ids_costs_and_depth_in_stats():
    trans = {"A": {"a": "B"}, "B": {"b": "C"}}
    costs = {("A", "a", "B"): 2.0, ("B", "b", "C"): 3.0}
    p = ChainProblem(start="A", goal="C", transitions=trans, costs=costs)
    path, stats = ids(p, max_limit=5, return_stats=True)
    assert stats.solution_cost == pytest.approx(5.0)
    assert stats.solution_depth == 2
