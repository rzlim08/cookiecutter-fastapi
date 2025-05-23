.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style
	@uv run ruff check app tests

test: ## run tests quickly with the default Python
	@uv run pytest . 

coverage: ## check code coverage quickly with the default Python
	@uv run coverage run --source . -m pytest
	@uv run coverage report -m
	@uv run coverage html

release: dist ## package and upload a release
	@uv run twine upload dist/*

dist: clean install-build ## builds source and wheel package
	@uv run python -m build --sdist --wheel 

install-build: clean ## install the package to the active Python's site-packages for packaging
	@uv pip install '.[build]'

install-dev: clean ## install the package to the active Python's site-packages for development
	@uv pip install -e '.[dev]'

install: clean ## install the package to the active Python's site-packages
	@uv pip install .

uv.lock: ## create uv lock file
	uv lock

#### Docker ################################################
export docker_compose_run:=docker compose run --rm
export docker_compose:=docker compose

.PHONY: docker-build
docker-build: ## Build docker containers
	$(docker_compose) build

.PHONY: init
init: uv.lock ## Initialize the local dev environment
	$(docker_compose) up -d
	$(MAKE) generate-migration
	$(MAKE) apply-migrations

.PHONY: up
up: ## Start the local dev environment
	$(docker_compose) up -d

.PHONY: down
down: ## Stop the local dev environment
	$(docker_compose) down

#### Migrations #############################################
.PHONY: apply-migrations
apply-migrations: ## Run alembic migrations locally
	$(docker_compose_run) {{cookiecutter.project_slug}} uv run alembic upgrade head

.PHONY: undo-migration
undo-migration: ## Downgrade the latest alembic migration
	$(docker_compose_run) {{cookiecutter.project_slug}} uv run alembic downgrade -1

.PHONY: show-migrations
show-migrations: ## Show the current alembic migration status
	$(docker_compose_run) {{cookiecutter.project_slug}} uv run alembic history

.PHONY: generate-migration
generate-migration: ## Create new alembic migrations files based on SA schema changes. Don't run unless you have actually changed the schema.
	$(docker_compose_run) {{cookiecutter.project_slug}} uv run alembic revision --autogenerate -m "autogenerated" --rev-id $$(date +%Y%m%d_%H%M%S)
