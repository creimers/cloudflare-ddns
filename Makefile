PYTHON := venv/bin/python
PIP := venv/bin/pip

all: install

$(PYTHON):
	-rm -rf venv
	virtualenv -p python3.7 venv

$(PIP): $(PYTHON)

install: $(PIP)
	$(PIP) install -r requirements.txt
