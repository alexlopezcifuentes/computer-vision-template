import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_docker = '{{cookiecutter.use_docker}}' == 'y'
create_code_quality = '{{cookiecutter.use_code_quality}}' == 'y'
create_hydra = '{{cookiecutter.use_hydra_config}}' == 'y'


if not create_docker:
    # Copy requirements.txt to parent directory
    shutil.copyfile(
        os.path.join(os.getcwd(), 'docker-dev', 'requirements.txt'),
        os.path.join(os.getcwd(), 'requirements.txt')
    )
    # remove docker-dev folder
    remove(os.path.join(os.getcwd(), 'docker-dev'))

if not create_code_quality:
    # remove .github folder
    remove(os.path.join(os.getcwd(), '.flake8'))
    remove(os.path.join(os.getcwd(), 'pyproject.toml'))
    remove(os.path.join(os.getcwd(), '.pre-commit-config.yaml'))

if not create_hydra:
    # remove hydra folder
    remove(os.path.join(os.getcwd(), 'config'))