import re
import nmap
num = True
regex = r"x\d[\d|\D]"

test_str = b'B\x03d\xaa\xd2\x00\xb5other\x05block\xffThe quick brown fox jumps over the lazy dog..\n'
final_load = b'B\x01Es\xb8\x07\xb4time'



# another_payload = b'B\x01\x8b\xe3\x10\x81\xb4time'
# print(test_str[:19])



aux = b'M\xb9\x00\x00\x00\x06\x01\x05\x00\x01\xff\x00'
machines_ips = "10.0.0.1-2"
ip = "172.18.1.1"
scan = nmap.PortScanner()
scan.scan(hosts=machines_ips,arguments="-p1-10000 -sN".format(ip))

print(scan.scanstats())
