## Build / Lint / Test

- Build: None (pure Python). Create virtualenv, install deps if any. The virtual environment will be installed in .venv. If it is missing `make .venv` will crate it.
- Run all tests: pytest
- Run single test: pytest path/to/test_file.py::test_name
- Lint: flake8 && black --check .

## Repo layout
- Source code: `src/`
- Tests: `tests/`

## Code style & guidelines
- Python 3.10+; use type hints for functions and methods where practical.
- Formatting: use Black (88 char line length) and isort for imports.
- Imports: standard library first, then third-party, then local;
- Naming: snake_case for functions and variables, PascalCase for classes, UPPER_SNAKE for constants.
- Types: prefer builtin typing (list, dict) for simple types; use typing.List, typing.Dict if required by project policy.
- Error handling: raise specific exceptions; avoid bare except; prefer defensive checks and clear error messages.
- Tests: unit tests should be deterministic and small; mock external IO.

## Agent rules
- Agents may create or edit files under `simple_search/` and `tests/` only.
- Agents must run `pytest` locally after changes and ensure tests pass before committing.

## Cursor / Copilot rules
- If `.cursor/rules/` or `.cursorrules` exist, follow them. If `.github/copilot-instructions.md` exists, follow Copilot instructions.

## Commit & PR
- Write concise commit messages describing why the change was made.
- Do not push directly to protected branches; create topic branches and PRs.

