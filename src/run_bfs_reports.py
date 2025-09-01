"""Shim that calls the consolidated run_reports CLI for BFS."""
from __future__ import annotations
import sys
from subprocess import run

if __name__ == "__main__":
    args = [sys.executable, "-m", "src.run_reports", "bfs"]
    if len(sys.argv) > 1:
        args.extend(sys.argv[1:])
    run(args)
