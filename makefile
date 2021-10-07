run:
	python flip_coins.py

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

lint: 
	pylint --disable=R,C app.py

test: 
	python -m pytest -vv --cov=flip_coins.py test_flip_coins.py