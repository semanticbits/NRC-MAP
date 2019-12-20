PROJECT=nrc-map
ifeq ("$(shell uname -s)", "Linux*")
	BROWSER=/usr/bin/firefox
else
	BROWSER=open
endif
MOUNT_DIR=$(shell pwd)
PKG_MANAGER=pip
PORT:=$(shell awk -v min=16384 -v max=32768 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')
NOTEBOOK_NAME=$(USER)_notebook_$(PORT)
SRC_DIR=/usr/src/nrc_map
USER=$(shell echo $${USER%%@*})
VERSION=$(shell echo $(shell cat nrc_map/__init__.py | \
			grep "^__version__" | \
			cut -d = -f 2))

.PHONY: upgrade-packages

deploy: docker-up
	docker container exec $(PROJECT)_python \
		pip3 wheel --wheel-dir=wheels .
	git tag -a v$(VERSION) -m "Version $(VERSION)"
	@echo
	@echo
	@echo Enter the following to push this tag to the repository:
	@echo git push origin v$(VERSION)

docker-down:
	docker-compose -f development/docker-compose.yaml down

docker-images-update:
	docker image ls | grep -v REPOSITORY | cut -d ' ' -f 1 | xargs -L1 docker pull

docker-rebuild: envfile setup.py
	docker-compose -f development/docker-compose.yaml up -d --build

docker-up:
	docker-compose -f development/docker-compose.yaml up -d

ipython: docker-up
	docker container exec -it $(PROJECT)_python ipython

notebook: docker-up notebook-server
	sleep 3
	${BROWSER} $$(docker container exec \
		$(USER)_notebook_$(PORT) \
		jupyter notebook list | grep -o '^http\S*')

notebook-remove:
	docker container rm -f $$(docker container ls -f name=$(USER)_notebook -q)

notebook-server:
	docker container run -d --rm \
		--name $(NOTEBOOK_NAME) \
		-p $(PORT):$(PORT) \
		-v `pwd`:/usr/src/$(PROJECT) \
		$(PROJECT)_python \
		/bin/bash -c "jupyter lab \
				--allow-root \
				--ip=0.0.0.0 \
				--no-browser \
				--port=$(PORT)"
	docker network connect $(PROJECT) $(NOTEBOOK_NAME)

snakeviz: docker-up snakeviz-server
	sleep 0.5
	${BROWSER} http://0.0.0.0:$(PORT)/snakeviz/

snakeviz-remove:
	docker container rm -f $$(docker container ls -f name=snakeviz -q)

snakeviz-server: docker-up
	docker container run -d --rm \
		--name snakeviz_$(PORT) \
		-p $(PORT):$(PORT) \
		-w /usr/src/$(PROJECT)/profiles \
		-v `pwd`:/usr/src/$(PROJECT) \
		$(PROJECT)_python \
		/bin/bash -c \
			"snakeviz profile.prof \
				--hostname 0.0.0.0 \
				--port $(PORT) \
				--server"
	docker network connect $(PROJECT) snakeviz_$(PORT)

tests: docker-up
	docker container exec $(PROJECT)_python \
		/bin/bash -c \
			"pytest \
				--basetemp=pytest \
				--cov=. \
				--cov-report html \
				--ff \
				-r all \
				-vvv"

tests-coverage: tests
	${BROWSER} htmlcov/index.html

upgrade-packages: docker-up
ifeq ("${PKG_MANAGER}", "pip")
	docker container exec $(PROJECT)_python \
		/bin/bash -c \
			"pip3 install -U pip \
			 && pip3 freeze | \
				grep -v NRC-MAP | \
				cut -d = -f 1 > requirements.txt \
			 && pip3 install -U -r requirements.txt \
			 && pip3 freeze > requirements.txt \
			 && sed -i -e '/^-e/d' requirements.txt"
else ifeq ("${PKG_MANAGER}", "conda")
	docker container exec $(PROJECT)_python \
		/bin/bash -c \
			"conda update conda \
			 && conda update --all \
			 && pip freeze > requirements.txt \
			 && sed -i -e '/^-e/d' requirements.txt"
endif
