#!/bin/bash

echo "make sure you ran docker-compose up [-d] before running this test"
echo "Access the selenium grid console at http://localhost:4444/grid/console"

pytest --driver Remote --capability browserName firefox test_pytest_selenium.py
