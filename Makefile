.PHONY: help test clean .coverage

TEST_VENV_NAME=testing_venv
TEST_PIP=${TEST_VENV_NAME}/bin/pip3

TEST_ISORT=${TEST_VENV_NAME}/bin/isort
TEST_FLAKE=${TEST_VENV_NAME}/bin/flake8
TEST_PYLINT=find . -type f -name "*.py" ! -path "./venv/*" ! -path "./testing_venv/*" | xargs ${TEST_VENV_NAME}/bin/pylint
TEST_MYPY=${TEST_VENV_NAME}/bin/mypy
TEST_BANDIT=${TEST_VENV_NAME}/bin/bandit
TEST_COVERAGE=${TEST_VENV_NAME}/bin/coverage

.DEFAULT: help

help:
	@echo "make test"
	@echo "       create testing virtualenv and run tests"
	@echo "make clean"
	@echo "       remove temporary files"

.testing-venv:
	@printf "Creating virtualenv...\t\t"
	@pip3 install -q virtualenv
	@virtualenv -q -p python3 $(TEST_VENV_NAME)
	@echo "\033[92m [OK] \033[0m"
	@printf "Installing requirements...\t"
	@${TEST_PIP} install -q -r requirements-dev.txt
	@echo "[OK]"

.isort:
	@echo "Running isort..."
	@${TEST_ISORT} -rc ./
	@echo "[Isort finished]"

.flake8:
	@printf "Running flake8 checks...\t"
	@${TEST_FLAKE} ./
	@echo "[OK]"

.pylint:
	@echo "Running pylint checks...\t"
	@${TEST_PYLINT}
	@echo "[OK]"

.mypy:
	@echo "Running mypy checks...\t"
	@${TEST_MYPY} ./


.bandit:
	@printf "Running bandit checks...\t"
	@${TEST_BANDIT} -r ./
	@echo "[OK]"

.coverage:
	@printf "Running coverage checks...\t"
	@${TEST_COVERAGE} run manage.py test
	@printf "Generating coverage report...\t"
	@${TEST_COVERAGE} report -m



test: .testing-venv .isort .flake8 .pylint .mypy .bandit .coverage

clean:
	@rm -rf build dist .eggs *.egg-info .coverage
	@rm -rf ${TEST_VENV_NAME}
	@rm -rf coverage_html_report
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +