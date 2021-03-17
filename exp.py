import zlib

data_string = "Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5Oliver is a bau5"
comped = zlib.compress(data_string.encode('utf-8'), level=-1).hex()
decomped = zlib.decompress(bytearray.fromhex(comped)).decode('utf-8')

print(len(data_string.encode('utf-8')))
print(comped)
print(decomped)

