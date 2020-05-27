.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  help          - show this message"
	@echo "  install       - install dependencies"
	@echo "  run           - run development server"

.PHONY: install
install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements/dev.txt

.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8000
