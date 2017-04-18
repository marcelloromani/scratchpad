#!/bin/bash

IMAGE_NAME=marcelloromani1975/centosbase_ssh_server:6.8
#IMAGE_NAME=centosbase_ssh_server:6.8

docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
