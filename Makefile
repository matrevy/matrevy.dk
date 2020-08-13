.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  css           - compile sass to css"
	@echo "  help          - show this message"
	@echo "  install       - install dependencies"
	@echo "  run           - run development server"

.PHONY: css
css:
	pysassc sass/main.scss static/css/main.css

.PHONY: install
install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements/dev.txt

.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8000
