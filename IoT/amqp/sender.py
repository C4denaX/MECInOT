import pika
import random
from time import sleep

creden = pika.PlainCredentials("test","test")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.1.65',credentials=creden))
channel = connection.channel()
try:
    channel.queue_declare(queue='hello')
except:
    pass

try:
    while True:
        number = random.randint(33,126)
        channel.basic_publish(exchange='', routing_key='hello', body=str(number))
        print(" [x] Sent " + str(number) )
        sleep(2)
finally:
    connection.close()
