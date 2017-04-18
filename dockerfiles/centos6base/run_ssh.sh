#!/bin/sh

SSH_PORT=2222

IMAGE_NAME=marcelloromani1975/centosbase:6.8
#IMAGE_NAME=centosbase:6.8

echo "Connec to the host with:"
echo "ssh -p $SSH_PORT admin@localhost"
echo "Password: admin"
echo
echo "To connect with key-based auth:"
echo "ssh -i `pwd`/files/id_rsa -p $SSH_PORT admin@localhost"

docker run --rm -it -p $SSH_PORT:22 $IMAGE_NAME /bin/sh -c 'sudo /etc/init.d/sshd start && /bin/bash'
