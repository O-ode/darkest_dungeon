python -m pip install --upgrade pip
python -m pip install --user pipenv
cd %~dp0
::pipenv --rm
python -m pipenv install --dev --skip-lock
pipenv run python main.py