include .env

.PHONY: clean
clean: clean_pyc

.PHONY: clean_pyc
clean_pyc:
	find . -name "*pyc" -exec rm -f {} \;


.PHONY: requirements
requirements:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

