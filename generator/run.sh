#!/bin/bash

# run tests
py.test --cov-append --junitxml=../test_reports/pytest-report.xml --cov-report xml:../test_reports/coverage.xml --cov-report term --cov=./ --cov-config=.coveragerc -v ./tests

# log error and remove test data
if [ $? -ne 0 ]; then
    echo "pytest: ERROR: Unit Testing has failed, see errors above"
    rm test_data/*
    exit 1
else
    rm test_data/*
fi

python vogtle_data_generator.py -d data/