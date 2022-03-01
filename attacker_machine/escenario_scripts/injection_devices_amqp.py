import pika
import random
from time import sleep
from scapy.all import *
from scapy.layers import *
import string
import threading
def sender_device(name):
    creden = pika.PlainCredentials("test","test")

    connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.1.65",credentials=creden))

    channel = connection.channel()

    try:
        channel.queue_declare(queue="hello")
    except:
        pass
    try:
        for i in range(0,10000):
            data = random.choice(string.ascii_letters)        
            channel.basic_publish(exchange="", routing_key="hello", body=data)
            print("[x] Sent by  " + name + ":" + data)
        
    finally:
        connection.close()

if __name__=="__main__":
    for i in range(0,8):
        name = "Thread-"+str(i)
        x = threading.Thread(target=sender_device, args=(name,))
        x.start()
        

