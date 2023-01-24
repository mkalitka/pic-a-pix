.PHONY: help all install setup clean uninstall lint format

_RED := "\033[31m%s\033[0m %s\n"

help:
	@echo "make"
	@echo "    help"
	@echo "        Display this message."
	@echo "    all"
	@echo "        Install pic-a-pix, linter and formatter."
	@echo "    install"
	@echo "        Install or update pic-a-pix."
	@echo "    setup"
	@echo "        Install linter and formatter."
	@echo "    clean"
	@echo "        Remove Python/build artifacts."
	@echo "    uninstall"
	@echo "        Uninstall pic-a-pix and its dependencies."
	@echo "    lint"
	@echo "        Lint code with pylint."
	@echo "    format"
	@echo "        Format code with black."

all: setup install

install:
	@echo "We suggest you to install this package within an virtual environment."
	@read -p "Do you want to continue? [Y/n] " ans && ans=$${ans:-Y} ; \
	if [ $${ans} = y ] || [ $${ans} = Y ] ; then \
		pip3 install -e . ; \
	else \
		printf ${_RED} "Installation cancelled." ; \
	fi

setup:
	@echo "We suggest you to setup this package within an virtual environment."
	@read -p "Do you want to continue? [Y/n] " ans && ans=$${ans:-Y} ; \
	if [ $${ans} = y ] || [ $${ans} = Y ] ; then \
		pip3 install black pylint ; \
	else \
		printf ${_RED} "Setup cancelled." ; \
	fi

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

uninstall: clean
	@pip3 uninstall pic_a_pix pillow pygame

lint:
	@pylint --disable C0114 --disable C0103 pic_a_pix/

format:
	@black .
