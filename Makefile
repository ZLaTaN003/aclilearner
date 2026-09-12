.PHONY: help tools test dist test_pypi pypi

help:
	echo "make <target>"

tools:	
	python -m pip install -e .

test:	
	python -m pytest

dist: 
	python -m build --sdist --wheel
	python -m twine check dist/*

test_pypi:
	python -m twine upload --verbose --repository testpypi dist/*

pypi:
	python -m twine upload --verbose dist/*