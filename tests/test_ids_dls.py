import pytest

from src.ids import depth_limited_search, IDSStats


class SimpleProblem:
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


def test_dls_start_is_goal():
    p = SimpleProblem(start="A", goal="A", transitions={})
    path, stats = depth_limited_search(p, limit=0, return_stats=True)
    assert path_states(path) == ["A"]
    assert stats.solution_depth == 0
    assert stats.solution_cost == 0.0


def test_dls_one_step():
    trans = {"A": {"toB": "B"}}
    p = SimpleProblem(start="A", goal="B", transitions=trans)
    # depth 0 -> no solution
    path = depth_limited_search(p, limit=0, return_stats=False)
    assert path == []
    # depth 1 -> solution
    path, stats = depth_limited_search(p, limit=1, return_stats=True)
    assert path_states(path) == ["A", "B"]
    assert stats.solution_depth == 1
    assert stats.solution_cost == 1.0


def test_dls_depth_blocks_solution():
    # chain A->B->C->D(goal)
    trans = {"A": {"a": "B"}, "B": {"b": "C"}, "C": {"c": "D"}}
    p = SimpleProblem(start="A", goal="D", transitions=trans)
    # limit 2 should fail
    path, stats = depth_limited_search(p, limit=2, return_stats=True)
    assert path == []
    assert stats.solution_depth is None
    # limit 3 should find
    path, stats = depth_limited_search(p, limit=3, return_stats=True)
    assert path_states(path) == ["A", "B", "C", "D"]
    assert stats.solution_depth == 3


def test_dls_branching_dfs():
    # A has two children B and C. B leads deep to goal, C is shallow dead-end.
    trans = {
        "A": {"goB": "B", "goC": "C"},
        "B": {"b1": "B1"},
        "B1": {"b2": "Goal"},
        "C": {}
    }
    p = SimpleProblem(start="A", goal="Goal", transitions=trans)
    path, stats = depth_limited_search(p, limit=3, return_stats=True)
    assert path_states(path)[-1] == "Goal"
    assert stats.solution_depth == 3


def test_dls_cycles_terminate():
    # A->B->A cycle, goal at C reachable from B
    trans = {"A": {"toB": "B"}, "B": {"toA": "A", "toC": "C"}, "C": {}}
    p = SimpleProblem(start="A", goal="C", transitions=trans)
    path, stats = depth_limited_search(p, limit=3, return_stats=True)
    assert path_states(path) == ["A", "B", "C"]
    assert stats.solution_depth == 2


def test_dls_stats_sanity():
    # binary tree of depth 2 from root A
    trans = {
        "A": {"a1": "B", "a2": "C"},
        "B": {"b1": "D", "b2": "E"},
        "C": {"c1": "F", "c2": "G"},
    }
    p = SimpleProblem(start="A", goal="X", transitions=trans)
    path, stats = depth_limited_search(p, limit=2, return_stats=True)
    # no solution
    assert path == []
    # nodes_generated should be 1 (root) + 2 (children) + 4 (grandchildren) = 7
    assert stats.nodes_generated == 7
    assert stats.nodes_expanded == 7
    assert stats.max_frontier_size >= 1


def test_dls_costs():
    trans = {"A": {"toB": "B"}, "B": {"toC": "C"}}
    costs = {("A", "toB", "B"): 2.5, ("B", "toC", "C"): 1.5}
    p = SimpleProblem(start="A", goal="C", transitions=trans, costs=costs)
    path, stats = depth_limited_search(p, limit=2, return_stats=True)
    assert stats.solution_cost == pytest.approx(4.0)


def test_dls_no_stats_return():
    trans = {"A": {"toB": "B"}}
    p = SimpleProblem(start="A", goal="B", transitions=trans)
    path_only = depth_limited_search(p, limit=1, return_stats=False)
    path_stats = depth_limited_search(p, limit=1, return_stats=True)[0]
    assert path_only == path_stats
