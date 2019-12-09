#!/bin/bash

# run tests
py.test --cov-append --junitxml=../tests/pytest-report.xml --cov-report xml:../tests/coverage.xml --cov-report term --cov=./ --cov-config=.coveragerc ./tests 

# cleanup test data
rm test_data/*

if [ $? -ne 0 ]; then
    echo "pytest: ERROR: Unit Testing has failed, see errors above"
    exit 1
fi

python vogtle_data_generator.py -d data/