FROM marcelloromani1975/centosbase:6.8

EXPOSE 22

ENTRYPOINT ["/bin/sh", "-c", "/home/admin/show_credentials.sh && sudo /etc/init.d/sshd start && sleep infinity"]
