# This make file is to setup python project environment

# Set up virtual environment
.PHONY: setup
setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

# Save all dependencies to requirements.txt
.PHONY: freeze
freeze:
	.venv/bin/pip freeze > requirements.txt

# Run the project
.PHONY: run
run:
	.venv/bin/python3 src/main.py

# Run the project with debug mode
.PHONY: debug
debug:
	.venv/bin/python3 src/main.py --debug

# Run tests with coverage
.PHONY: test
test:
	PYTHONPATH=./src .venv/bin/pytest tests/

# Run lint over src and tests, show only errors
.PHONY: lint
lint:
	.venv/bin/pylint src/ tests/ --errors-only

# Clean up all temporary files (including .venv)
.PHONY: clean
clean:
	@echo "Cleaning up..."
	@rm -rf .venv
	@find . \( -type f -name "*.pyc" -or \
	           -type d -name "__pycache__" -or \
	           -type d -name ".pytest_cache" -or \
	           -type d -name ".mypy_cache" -or \
	           -type d -name ".coverage" -or \
	           -type d -name ".cache" \) -exec rm -rf {} +
	@echo "Clean up complete."
# Clean, Setup, Test and Run
.PHONY: all
all: clean setup test run

# Install package (receiving package names as param) and freeze
.PHONY: install
install:
# Check if pkgs is empty
ifndef pkgs
	$(error pkgs is undefined, Usage: make install pkgs="<package1> <package2> ..." (don't forget the quotes))
endif
	@echo "Installing packages..."
	.venv/bin/pip install $(pkgs)
	.venv/bin/pip freeze > requirements.txt
	@echo "Installation complete."