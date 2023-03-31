.DEFAULT_GOAL := help
.PHONY: help

help:
	@echo "Make sure you have poetry installed"
	@echo "You also need the poetry plugin up, install with poetry self add poetry-plugin-up"
	@echo "If this is the first time that you run this project, please run "make install" prior to any action"

install:
	poetry up --latest

format-notebook:
	nbqa black *.ipynb
	nbqa isort *.ipynb