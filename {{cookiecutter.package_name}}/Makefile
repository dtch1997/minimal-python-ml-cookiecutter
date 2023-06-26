.venv:
	python -m venv .venv
	touch .venv

.install_requires:
	.venv/bin/python -m pip install -r requirements/base.txt
	.venv/bin/python -m pip install -r requirements/dev.txt
	.venv/bin/python -m pip install -e .
	pre-commit install

test: 
	.venv/bin/python -m pytest -m pytest tests --cov=llm_curriculum --cov-report=xml

install: .venv .install_requires

all: install test

.PHONY: .install_requires install test all