import pika
import random
from time import sleep

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.0.0.4'))
channel = connection.channel()

channel.queue_declare(queue='hello')
try:
    while True:
        number = random.randint(0,100)
        channel.basic_publish(exchange='', routing_key='hello', body=str(number))
        print(" [x] Sent " + str(number) )
        sleep(2)
finally:
    connection.close()
