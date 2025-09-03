from simple_search.reports import run_reports
from simple_search.problems.eight_puzzle import EightPuzzleState, EightPuzzleProblem


def test_print_report_bfs_shallow(capsys):
    one_move = EightPuzzleState((1, 2, 3, 4, 5, 6, 7, 0, 8))
    prob = EightPuzzleProblem(start=one_move)
    run_reports.print_report(prob, "bfs")
    captured = capsys.readouterr()
    assert "Algorithm: BFS" in captured.out
    assert "Depth: 1" in captured.out


def test_print_report_ids_shallow(capsys):
    two_move = EightPuzzleState((1, 2, 3, 4, 5, 6, 0, 7, 8))
    prob = EightPuzzleProblem(start=two_move)
    run_reports.print_report(prob, "ids")
    captured = capsys.readouterr()
    assert "Algorithm: IDS" in captured.out
    assert "Depth: 2" in captured.out
