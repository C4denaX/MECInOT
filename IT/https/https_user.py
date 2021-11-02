import requests,os
from time import sleep
from random import randint
try:
    while True:    
        r = requests.get("https://10.0.0.9", verify=False)

        print(r.status_code)
        sleep(randint(1,3))

except KeyboardInterrupt:
    os._exit(0)
