[[ ! -d ".venv" ]] && virtualenv .venv
poetry install
poetry run pre-commit install
