# justfile for uv + pytest workflow

# Create a uv virtual environment
venv:
	uv venv

# Install project in editable mode + pytest
install:
	uv pip install -e .
	uv pip install pytest

# Run smoke/unit tests (calls pytest inside uv env)
test:
	uv run pytest

# Run the console script directly through uv
run:
	uv run python -m what is love

# Clean venv + build artifacts
clean:
	rm -rf .venv dist *.egg-info __pycache__ */__pycache__
