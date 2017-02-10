#!/bin/bash

echo "make sure you ran docker-compose up [-d] before running this test"

if [ $# != 1 ] ; then
    echo "usage: $0 <number_of_instances>"
    exit 1
fi

docker-compose scale firefox=$1
