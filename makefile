PYTHON =python3
SRC_DIR=.

all:
	$(PYTHON) gatorLibrary.py test1.txt

test:
	$(PYTHON) gatorLibrary.py test1.txt
	$(PYTHON) gatorLibrary.py test2.txt
	$(PYTHON) gatorLibrary.py test3.txt
	$(PYTHON) gatorLibrary.py test4.txt
	$(PYTHON) gatorLibrary.py Example1.txt
	$(PYTHON) gatorLibrary.py Example2.txt
	$(PYTHON) gatorLibrary.py Example3.txt

