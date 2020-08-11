SHELL := /bin/zsh

export PIPENV_IGNORE_VIRTUALENVS=1

.PHONY: run
run: build
	@echo "Starting Application."
	pipenv run python decisions

.PHONY: build
build: clean
	@echo "Starting build."
	cp -r decisions build
	@echo "Build complete."

.PHONY: clean
clean:
	@echo "Cleaning build directory."
	find ./build -exec rm {} \;

.PHONY: test
test:
	pipenv run pytest --cov=decisions --cov-report html

.PHONY: coverage
coverage: test
	open htmlcov/index.html
