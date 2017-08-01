echo "executing build step!!!"
echo $PWD
whoami

coverage-3.6 run --source=younit run_tests.py --unit --integration --output xml --dist ubuntu
coverage xml
coverage html