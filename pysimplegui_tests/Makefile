.PHONY: venv

help:
	@echo "Sample apps using PySimplwGUI"
	@echo
	@echo "macos            install required tcl-tk libraries on MacOS using 'brew'"
	@echo "venv             create a virtualenv in folder 'venv'"
	@echo "requirements     install requirements"
	@echo "run              run the sample code"

venv:
	@python3 -m venv venv && echo "Activate virtualenv with: . venv/bin/activate"

requirements:
	. venv/bin/activate && pip install -r requirements.txt

macos:
	brew install tcl-tk
	brew install python-tk

run-empty-window:
	. venv/bin/activate && python empty-window.py

run-login-form:
	. venv/bin/activate && python login-form.py

run-pattern-1a:
	. venv/bin/activate && python pattern-1a.py
