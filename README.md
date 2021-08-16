# E-Commerce microservice

### Run tests

During tests launches, a virtual environment `testing_venv` is created, packages from `requirements-dev.txt` are
 installed, and several code check programs are launched.

Tests includes:

- run `isort`
- run `flake8`
- run `pylint`
- run `mypy`
- run `bandit`

To run all tests:

```bash
$ make test
``` 

To clean working directory from temporary files and folders which were created after test checks, run in bash:

```bash
$ make clean
```

### Environment variables

All environment variables and its defaults are set in settings

**PostgreSQL credentials**

- `DB_USER` - PostgreSQL user
- `DB_PASSWORD` - PostgreSQL password
- `DB_HOST` - PostgreSQL host URL
- `DB_NAME` - PostgreSQL db name

**Sentry settings**
- `SENTRY_DSN` - Sentry DSN
- `SENTRY_ENV` - Sentry environment name

**Other settings**

- `ENV` - default: `debug`

## Authors

- Andrey Butynin
