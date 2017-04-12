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
COPY ./motd /etc/motd
RUN echo "cat /etc/motd" >> /etc/bash.bashrc

USER admin
WORKDIR /home/admin
