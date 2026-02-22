.PHONY: install test lint run

install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -e .[dev]

test:
	pytest -q

lint:
	ruff check src tests

run:
	python -m src.main
