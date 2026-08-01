run:
	python -m sessiond

lint:
	ruff check src tests

format:
	black src tests
