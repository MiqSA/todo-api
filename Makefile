SRC_DIR_APPS = tests
DOCKER_COMPOSE_FILE = infra/docker-compose.yml
PROJECT_NAME = todo_api

run: ## Run the API
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

run-prod: ## Run the API like in prod
	gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.main:app

lint: ## Run code linters
	flake8 $(SRC_DIR_APPS)

cover: ## Generate test coverage report in xml
	coverage run -m pytest	
	coverage xml

cover-html: ## Generate test coverage report in html
	coverage html

test: ## Run specified tests
	pytest -v $(SRC_DIR_APPS) 

tests: ## Run tests
	pytest -v

deps-up: ## To up all dependencies
	docker compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) up -d

deps-down: ## To down all dependencies
	docker compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) down

deps-rebuild: ## To rebuild all dependencies
	docker compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) down
	docker compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) up --build -d

help:
	@echo "Available targets:"
	@egrep -o "^([a-zA-Z_-]+):.*?## (.+)" $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s - %s\n", $$1, $$2}' | sort

%:
	@echo "Unknown target. Run 'make help' for available targets." >&2
	@exit 1