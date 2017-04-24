FROM ubuntu:16.04
RUN apt-get -qy update && \
    apt-get -qy install   \
    vim            \
    less           \
    net-tools      \
    iputils-ping   \
    host           \
    openssh-server \
    git            \
    tmux           \
    links2         \
    sudo        && \
    apt-get -y autoremove

RUN adduser --system --ingroup sudo --shell /bin/bash admin
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
