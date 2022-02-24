import snap7

from time import sleep


import random
client = snap7.client.Client()

client.connect("10.0.0.1",0,0,102)

print(client.get_connected())

try:
    while True:

        data = client.db_read(1,0,20)
        sleep(random.randint(1,6))
        print(data.decode())

except KeyboardInterrupt:
    client.destroy()
