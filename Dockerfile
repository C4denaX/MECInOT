FROM ubuntu:trusty

RUN apt-get update && apt-get install -y \
	software-properties-common && \
	apt-add-repository ppa:mosquitto-dev/mosquitto-ppa && \
	apt-get update && apt-get install -y \
	python3 \
	mosquitto \
	python3-pip \
	net-tools \
	openssh-server

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 user

RUN  echo 'user:user' | chpasswd
RUN service ssh start

ADD * /
RUN pip3 install -r requeriments.txt




