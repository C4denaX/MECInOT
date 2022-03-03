FROM kalilinux/kali-rolling
WORKDIR /home/kali
COPY escenario_scripts/ .

RUN apt update && apt -y install dsniff hydra-gtk python3 net-tools iputils-ping ncat nmap vim python3-scapy wordlists python2 metasploit-framework python3-pip
RUN pip3 install python-pip




