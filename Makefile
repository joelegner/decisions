SHELL := /bin/zsh

export PIPENV_IGNORE_VIRTUALENVS=1

.PHONY: run
run: build
	@echo "Starting Application."
	pipenv run python build/src/run.py

.PHONY: build
build: clean
	@echo "Starting build."
	cp -r src build
	@echo "Build complete."

.PHONY: clean
clean:
	@echo "Cleaning build directory."
	rm -Rf build/*
