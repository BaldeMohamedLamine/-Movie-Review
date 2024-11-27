.PHONY: install_dev
install_dev:
	python -m pip install -r requirements.txt
	pre-commit install


.PHONY: start_docker_compose
start_docker_compose:
	docker compose up


.PHONY: test
test:
	pytest tests --cov --cov-report term-missing

.PHONY: run
run:
	python manage.py runserver


.PHONY: superuser
superuser:
	python manage.py createsuperuser


.PHONY: migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate



.PHONY: help
help:
	@echo Available commands:
	@echo   install_dev         - Install dependencies and set up pre-commit"
	@echo   start_docker_compose - Start Docker containers for testing"
	@echo   test                - Run tests with coverage report"
	@echo   run_dev             - Run Django development server"
	@echo   superuser           - Create a Django superuser"
	@echo   migrate             - Apply database migrations"
