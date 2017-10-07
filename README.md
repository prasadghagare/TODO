steps to start the project

git clone the project

source .venv/bin/activate

pip install -e .

export FLASK_APP=manage.py

export FLASK_DEBUG=1

flask initdb

flask run

In other terminal : cd to project directory

source .venv/bin/activate

python tests/functional_tests.py -- functional_tests

python todo/tests.py

limitation removed in v0.2
