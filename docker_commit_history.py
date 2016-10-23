#!/usr/bin/env python
"""
Goal:
    Show commit messages of a docker image recursively,
    similar to what git log --oneline would output.

Current output:
    It consists of three columns:
    Image id (first 12 characters)
    Author name
    Commit message

Example:
    mar@host:~$ sudo docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
    mar/ubuntu      dev                 7684a7333c71        44 minutes ago      274.1 MB

    mar@host:~$ ./docker_log.py 7684a7333c71
    7684a7333c7 "Marcello Romani" "Installed tcl"
    169c17ce1a8 "Marcello Romani" "Installed vim"
    b7f9dc853fc "Marcello Romani" "Installed git"
    5ba9dab4745 "" ""
    51a9c7c1f8b "" ""
    5f92234dcf1 "" ""
    27d47432a69 "" ""
    511136ea3c5 "" "Imported from -"
"""

import sys
import subprocess
import json


def print_commit(image_id):
    """
    Print info about the specified image commit; return the parent image id, if any
    """
    # todo check whether "sudo" is needed or not on the system
    json_obj = json.loads(subprocess.check_output(["sudo", "docker", "inspect", image_id]))

    image_id  = json_obj[0]["Id"]
    if ':' in image_id:
        image_id  = image_id.split(':')[1]
    comment   = json_obj[0]["Comment"]
    parent_id = json_obj[0]["Parent"]
    author    = json_obj[0]["Author"]

    print "%s \"%s\" \"%s\"" % (image_id[0:11], author, comment)

    return parent_id


def print_usage():
    print "Usage: docker_log.py <image id>"


def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    # print data from first commit
    parent_id = print_commit(sys.argv[1])

    # go on until the commit has a parent image
    while len(parent_id) > 0:
        parent_id = print_commit(parent_id)

if __name__ == "__main__":
    main()
