## Cookiecutter-FastAPI
* A cookiecutter template for setting up a simple fastapi project
* Code first, configuration later

### How to run this: 
If you have `uv` installed already just run:
```
uvx cookiecutter git@github.com:rzlim08/cookiecutter-fastapi.git
```

Otherwise try:

```
pip install -U cookiecutter 
```
or 

```
brew install cookiecutter # for macos
```

```
cookiecutter git@github.com:rzlim08/cookiecutter-fastapi.git
```

A cookiecutter template heavily influenced by: 

https://github.com/audreyfeldroy/cookiecutter-pypackage


* Simpler and more opinionated than the above package
* Commits to a more modern structure. I found it confusing that the above package contains `requirements-dev.txt`, `pyproject.toml`, `setup.py` etc. It makes it difficult to know which files to change to make configurations. 
* No doc building (yet). I might add this in later, but I find that this just confuses things. 

* The goal is to simply be able to use the `cookiecutter` command, install the package, and be able to run `make up`. This way the *first* thing that coders need to worry about is coding. 

### The Stack

## Development
* `coverage`
* `pytest`
* `mypy`
* `ruff`
* `Makefile` - for workflow coordination
* `pyproject.toml` - for all python packaging/distribution configuration

## Web
* `fastapi`
* `alembic` - migrations
* `pydantic` - input validation
* `sqlalchemy` - database connection

## Database
* `postgresql`
