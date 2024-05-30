PYTHON =python3
SRC_DIR=.

all:
	$(PYTHON) gatorLibrary.py test1.txt

test:
	$(PYTHON) gatorLibrary.py test1.txt
	$(PYTHON) gatorLibrary.py Example1.txt

