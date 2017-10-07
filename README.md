#steps to start the project
#cd Desktop/projects/TDD_App/TODO/
#source .venv/bin/activate
#pip install -e .
#export FLASK_APP=todo
#export FLASK_DEBUG=1
#flask initdb
#flask run
#In other terminal : cd Desktop/projects/TDD_App/TODO/
#source .venv/bin/activate
#python tests/functional_tests.py -- functional_tests
#python todo/tests.py
#c.execute('''CREATE TABLE item
#             (name text)''')
#limitation at this point : test and application DB are coupled
#so the changes made by tests to database are same as of the application
#delete the database created in cd /tmp to run functional_tests
