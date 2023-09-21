install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	#python3 -m pytest --nbval *.ipynb
	python3 -m pytest -vv --cov=main test_*.py

format:
	black *.py
	#nbqa black *.ipynb

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py 
	#ruff linting is 10-100X faster than pylint
	ruff check *.py
	#nbqa ruff *.ipynb

all: install lint format test
