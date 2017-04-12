#!/bin/bash

#IMAGE_NAME=marcelloromani1975/centosbase:6.8
IMAGE_NAME=centosbase:6.8

docker build -t $IMAGE_NAME .
#docker push
