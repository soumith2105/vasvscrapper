if [ ! -d ".venv" ]
then
  virtualenv .venv
fi
poetry install
poetry run pre-commit install