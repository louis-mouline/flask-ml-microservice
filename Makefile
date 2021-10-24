install:
	pip install --upgrade pip --user &&\
		pip install -r requirements.txt --user

test:
	python -m pytest -vv --cov=application --cov=utils/data --cov=utils/mllib test/test_mllib.py test/test_data.py

format:
	python -m black *.py utils/*.py test/*.py

lint:
	python -m pylint --disable=R,C,W1203,E1101 test/test_data test/test_mllib utils/data utils/mllib

all: install lint test