install:
	pip install --upgrade pip --user &&\
		pip install -r requirements.txt --user

test:
	python -m pytest -vv --cov=cli --cov=mlib --cov=utilscli test_mlib.py

format:
	python -m black *.py utils/*.py test/*.py

lint:
	python -m pylint --disable=R,C,W1203,E1101 mllib cli utilscli

all: install lint test