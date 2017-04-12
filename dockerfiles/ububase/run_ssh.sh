#!/bin/sh

SSH_PORT=2222

echo "Connecto the host with:"
echo "ssh -p $SSH_PORT admin@localhost"
echo "Password: admin"
echo
echo "To connect with key-based auth:"
echo "ssh -i `pwd`/files/id_rsa -p $SSH_PORT admin@localhost"

docker run --rm -it -p $SSH_PORT:22 test /bin/sh -c 'sudo service ssh start && /bin/bash'
