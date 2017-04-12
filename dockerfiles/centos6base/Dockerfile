FROM centos:6.8
RUN yum update -y && \
    yum install -y \
    vim            \
    less           \
    net-tools      \
    iputils-ping   \
    host           \
    openssh-server \
    git            \
    tmux           \
    links2         \
    sudo

RUN adduser --system -m -U --shell /bin/bash admin
RUN echo "admin:admin" | chpasswd
COPY files/motd /etc/motd
RUN echo "cat /etc/motd" >> /etc/bash.bashrc

COPY files/sudoers_admin /etc/sudoers.d/admin

USER admin
WORKDIR /home/admin

RUN mkdir .ssh
COPY files/id_rsa .ssh/
COPY files/id_rsa.pub .ssh/
COPY files/id_rsa.pub .ssh/authorized_keys
