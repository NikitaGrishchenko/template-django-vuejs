# Including commands
run-django-server:
	python ./backend/manage.py runserver

run-webpack-server:
	yarn serve

open-localhost:
	python -m webbrowser "http://localhost:8000"

# .PHONY: clear
# clear:
# 	poetry run task clear
.PHONY: venv-linux
venv-linux:
	python3 -m venv .venv
	source .venv/bin/activate;

.PHONY: venv-win
venv-win:
	touch .venv\Scripts\activate

.PHONY: createadmin
createadmin:
	python ./backend/manage.py createsuperuser

.PHONY: migrate
migrate:
	python ./backend/manage.py migrate


# Primary commands
.PHONY: install
install:
	pip install -r requirements.txt
	yarn
	@make migrate

.PHONY: install-prod
install-prod:
	poetry install --no-root
	yarn
	poetry run task initconfig

.PHONY: run
run:
	@make -j 3 run-django-server run-webpack-server open-localhost

.PHONY: build
build:
	yarn build
	poetry run task collectstatic
	@make migrate

.PHONY: deploy
deploy:
	@make build
	sudo systemctl restart gunicorn
	sudo systemctl restart nginx

.PHONY: docker-run
docker-run:
	poetry run task dockervolumes
	docker-compose up
