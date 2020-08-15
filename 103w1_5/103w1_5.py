data = [100,24,255]
buffer: bytes = bytes(data)
print(buffer)
f = open("binary.txt", "bw")
f.write(buffer)
f.close()
