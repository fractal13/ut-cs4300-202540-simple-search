PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest
BLACK := $(VENV)/bin/black
FLAKE8 := $(VENV)/bin/flake8

# create venv and install minimal test deps
.PHONY: all
all: test

$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install pytest

# run full test suite; allow extra pytest args via PYTEST_ARGS env var
.PHONY: test
test: $(VENV)
	$(PYTEST) $(PYTEST_ARGS)

# run a single test; usage: make test-single TEST=tests/test_bfs.py::test_name
.PHONY: test-single
test-single: $(VENV)
	$(PYTEST) $(TEST)

.PHONY: lint
lint: $(VENV)
	$(PIP) install black flake8
	$(BLACK) .
	$(FLAKE8) .

.PHONY: clean
clean:
	-rm -rf $(VENV)
	-find . -name '__pycache__' -type d -exec rm -rf {} +
