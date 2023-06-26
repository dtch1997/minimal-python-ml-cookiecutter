.venv:
	python -m venv .venv
	touch .venv

requirements/base.txt requirements/dev.txt: requirements/base.in requirements/dev.in .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install pip-tools
	.venv/bin/python -m piptools compile requirements/base.in -o requirements/base.txt
	.venv/bin/python -m piptools compile requirements/dev.in -o requirements/dev.txt
	touch requirements/base.txt
	touch requirements/dev.txt

compile: requirements/base.txt requirements/dev.txt

.install_requires:
	.venv/bin/python -m pip install -r requirements/base.txt
	.venv/bin/python -m pip install -r requirements/dev.txt
	.venv/bin/python -m pip install -e .
	pre-commit install

test: 
	.venv/bin/python -m pytest -m pytest tests --cov=llm_curriculum --cov-report=xml

install: .venv compile .install_requires

all: install test

.PHONY: .install_requires install test all