import array as arr
with open('test.bin','b+r') as input_file:
    # 讀出整數
    int_array = arr.array('i')   # 'i'表示資料是整數
    int_array.fromfile(input_file, 3)   # 讀出3個
    for item in int_array:
        print(item)

    # 讀出浮點數
    float_array = arr.array('d')
    float_array.fromfile(input_file, 2)   # 讀出2個
    for item in float_array:
        print(item)