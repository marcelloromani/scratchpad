#!/bin/bash

set -e
set -u

if [ $# != 2 ] ; then
    echo "Usage: $0 <container_name> <ssh_port>"
    echo "Example: $0 ssh_server 2222"
    exit 1
fi

IMAGE_NAME=marcelloromani1975/ububase:16.04-ssh
#IMAGE_NAME=ububase:16.04-ssh

CONTAINER_NAME=$1
SSH_PORT=$2

echo "Creating container $CONTAINER_NAME ..."
echo "SSH server listening on localhost:$SSH_PORT"
echo "To stop the container: docker rm -f $CONTAINER_NAME"

docker run --rm -d -p $SSH_PORT:22 --name $CONTAINER_NAME $IMAGE_NAME
