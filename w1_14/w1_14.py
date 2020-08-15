print("Hi, I am Marvin, your personal bot.")
print("lets add some numbers")
try:
    input1 = int(input("Number 1> "))
    input2 = int(input("Number 2> "))
except ValueError as e:
    print(print("Value error: {0}".format(e)))
    exit(-1)
result = input1 + input2
print(result)