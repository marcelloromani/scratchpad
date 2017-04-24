#!/bin/bash

IMAGE_NAME=marcelloromani1975/ububase:16.04-ssh
#IMAGE_NAME=ububase:16.04-ssh

docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
