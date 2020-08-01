SHELL := /bin/zsh

.PHONY: all
all: run

.PHONY: run
run:
	echo "Starting Decisions..."; \
	pipenv run python src/run.py
