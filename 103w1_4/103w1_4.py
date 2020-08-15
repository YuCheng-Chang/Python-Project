i=0
with open("test.txt") as f:
    for data in f:
        i+=int(data)
    print("sum="+str(i))