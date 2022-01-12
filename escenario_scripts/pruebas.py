import re
num = True
regex = r"x\d[\d|\D]"

test_str = b'B\x03d\xaa\xd2\x00\xb5other\x05block\xffThe quick brown fox jumps over the lazy dog..\n'
final_load = b'B\x01Es\xb8\x07\xb4time'



another_payload = b'B\x01\x8b\xe3\x10\x81\xb4time'
print(test_str[:19])