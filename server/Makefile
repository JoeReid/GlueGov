OS = $(shell uname -s)

INI_DEV  = development.ini
INI_TEST = test.ini
INI_PROD = production.ini


PROJECT=gluegov

help:
	# Usage: make <target>, where target is
	# install        -- run after clean checkout to pull dependecys and setup


.installed_python: .installed_python_$(OS)
	touch .installed_python

# OSX installation
.installed_python_Darwin:
	brew install python3
	# brew install gettext
	# cd ~/bin/ && ln -s /usr/local/opt/gettext/bin/msgmerge
	# python virtualenv?
	touch .installed_python_Darwin

# Linux installation
.installed_python_Linux:
	# apt-get install gettext
	if dpkg -s python-virtualenv ; then \
		echo virtualenv already installed; \
	else \
		echo installing virtualenv; \
		sudo apt-get install -y python-virtualenv curl; \
	fi
	if dpkg -s python3-setuptools ; then \
		echo python 3 already installed; \
	else \
		echo installing python 3; \
		sudo apt-get install -y python3-setuptools python3-dev curl; \
	fi
	touch .installed_python_Linux

env: .installed_python
	# Reference - http://docs.pylonsproject.org/projects/pyramid/en/1.5-branch/narr/install.html
	virtualenv --no-site-packages -p python3 env
	env/bin/easy_install pyramid

# Experiments
#env/bin/node: env
#	env/bin/pip install nodeenv
#	source env/bin/activate && nodeenv --python-virtualenv --prebuilt
#env/lib/node_modules/bower: env/bin/node
#	source env/bin/activate && npm install -g bower

GlueGov.egg-info: env
	env/bin/python setup.py develop

# Force reexecution of setup.py dependenys (this must be done from the Makefile or make gets confused and repetedy runs the task)
setup: GlueGov.egg-info
	env/bin/python setup.py develop

dependency_downloader.py:
	curl https://raw.githubusercontent.com/calaldees/libs/master/python3/lib/dependency_downloader.py --compressed -O

externals:
	mkdir externals && touch externals/__init__.py

dependency_download: dependency_downloader.py externals
	# Trigger dependency check on every startup
	env/bin/python dependency_downloader.py --destination externals
	#source env/bin/activate && bower install --config.interactive=false --config.directory=./externals/

data_folder:
	mkdir -p data

install: development.ini GlueGov.egg-info dependency_download data_folder


# Ini files --------------------------------------------------------------------

development.ini:
	cp development.ini.dist development.ini


run: install
	env/bin/pserve --reload $(INI_DEV)


shell: install
	env/bin/pshell $(INI_DEV)

# Clean ------------------------------------------------------------------------

clean_ini:
	rm -f $(INI_DEV)
	rm -f $(INI_TEST)
	rm -f $(INI_PROD)

clean: clean_ini
	rm -rf env
	rm -rf data
	rm -rf *.egg-info
	rm -f *.db
	rm -f *.log
	rm -rf externals
	rm -rf dependency_downloader.py
	rm -rf dependencys_installed.json
	rm -rf .installed_*
