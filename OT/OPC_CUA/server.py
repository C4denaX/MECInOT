import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server


import random

import string


def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str



if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients

    # starting!
    server.start()
    
    try:
        count = 0
        while True:
            time.sleep(random.randint(1,9))
            count += 0.1
            myvar.set_value(get_random_string(10))
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
