#!/bin/bash

echo "make sure you ran docker-compose up [-d] before running this test"

pytest --driver Remote --capability browserName firefox test_pytest_selenium.py
