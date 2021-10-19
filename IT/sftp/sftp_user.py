import paramiko,os
from time import sleep
from random import randint
try:
    while True:
        trans = paramiko.Transport(("10.0.0.8",22))

        trans.connect(username="foo",password="pass")

        client = paramiko.SFTPClient.from_transport(trans)

        print(client.listdir("/"))

        client.close()
        trans.close()
        sleep(randint(1,4))
except KeyboardInterrupt:
    os._exit(0)