import snap7

from time import sleep

import random

import string


def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str


client = snap7.client.Client()

client.connect("10.0.0.1",0,0,102)

print(client.get_connected())


try:
    while True:
        data = get_random_string(20)
        print("[*] Message send: " + data)
        data = bytearray(data.encode())
        client.db_write(1,0,data)
        sleep(random.randint(0,7))
except KeyboardInterrupt:
    client.destroy()



client.destroy()
