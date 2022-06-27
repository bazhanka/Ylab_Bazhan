def int32_to_ip(int32):
    return '.'.join([str(int32 >> (i << 3) & 0xFF) for i in range(0, 4)[::-1]])
print(int32_to_ip(2154959208))

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
