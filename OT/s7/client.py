import snap7

client = snap7.client.Client()

client.connect("192.168.1.65",0,0,1102)

print(client.get_connected())

data = client.db_read(1,0,4)

print(data)

data[3] = 0b00000001

client.db_write(1,0,data)

print(client.db_read(1,0,4))

client.destroy()
