from optparse import OptionParser
import paho.mqtt.client as mqtt
from threading import Thread, Condition
import time
import random

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
	if("topic" in msg.topic):
		print(msg.payload.decode("utf-8"))

if __name__=='__main__':
	parser = OptionParser(usage="%prog -b <broker-IP>")
	
	parser.add_option("-b", "--brokerip", action="store", dest="brokerip", metavar="<broker-IP>", default="localhost", help="MQTT broker IP. Default is localhost")
	
	(options, args) = parser.parse_args()
	broker_ip = "10.0.0.1"
	port = 1883
	mqtt_client = mqtt.Client()
	mqtt_client.on_connect = on_connect
	mqtt_client.on_message = on_message
	mqtt_client.connect(broker_ip, port, 60)
	mqtt_client.subscribe("topic")
	mqtt_client.loop_start()
	while True:
		time.sleep(1)
		mqtt_client.publish("topic", "temp:" + str(random.randint(20,45)))
	
