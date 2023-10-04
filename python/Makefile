.PHONY: all

help:
	@echo "help"

venv:
	python3 -m venv venv

requirements: venv
	. venv/bin/activate && pip install -r requirements.txt

requirements-dev: venv
	. venv/bin/activate && pip install -r requirements_dev.txt

test: unit-tests integration-tests

unit-tests: requirements-dev
	pytest -s -r A -k 'not Integration' --cov=main.py --cov=src --cov-report=html

integration-tests: requirements-dev
	pytest -s -r A -k 'Integration' --cov=main.py --cov=src --cov-report=html
