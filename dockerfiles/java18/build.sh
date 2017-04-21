#!/bin/bash
set -e
set -u

IMAGE_NAME="marcelloromani1975/centosbase_ssh_server:java-1.8"

docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
