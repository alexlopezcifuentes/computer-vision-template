initialize_git:
	@echo "Initializing git..."
	git init
	git add .
	git commit -m "Initial commit"

{%- if cookiecutter.use_code_quality == 'y' %}
	pre-commit install
{%- endif %}

{%- if cookiecutter.use_docker == 'y' %}
# Docker
docker-build:
	@echo "Building docker image..."
	docker build -t {{cookiecutter.project_slug}} . -f docker-dev/Dockerfile

setup: initialize_git docker-build
{%- endif %}


{%- if cookiecutter.use_code_quality == 'y' %}
# Quality Checks
flake8:
	flake8 .
isort-check:
	isort --check-only . --profile black
isort:
	isort . --profile black
black-check:
	black --check .
black:
	black .
{%- endif %}


{%- if cookiecutter.use_code_quality == 'y' %}
quality-check: isort-check black-check flake8
quality: isort black flake8
{%- endif %}
