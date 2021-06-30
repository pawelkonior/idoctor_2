# Django Quick


## Commands:

```bash
# Creating project
django-admin startproject <project_name>

# Running server
./manage.py runserver

# Creating app
django-admin startapp <app_name>


# Show all commands
./manage.py

```

## Virtual Environment commands (pipenv):

You can use any virtual env package (like virtualenv) but pipenv is the best for project like django because stores all versions of packages and dependencies with theirs hashes.

Pipfile and Pipfile.lock you should store in repository.
```bash

pip install pipenv
pipenv shell
pipenv install django==3.1

pipenv -h
pip freeze > requirements.txt

```

## Test Coverage commands (coverage):

```bash

pipenv install coverage

coverage run --omit='*/venv/*' manage.py test

coverage report
coverage html
open ./htmlcov/index.html

```

## Create project from template:

If you need something more powerful use:
[cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

```bash

# Creating template
mkdir project-name && cd project-name
# prepare virtual env

django-admin startproject project_name .

# open project and rename <project_name> to <{{ project_name }}> in all files

# Using template
django-admin startporject --template <path or URI> <project_name> .

# Working example
django-admin startproject --template https://github.com/pawelkonior/django_template/archive/master.zip new_latest_proj .

```