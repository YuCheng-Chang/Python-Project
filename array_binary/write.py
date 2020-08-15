
with open('test.bin', 'w+b') as output_file:
    import array as arr
    # 把要寫入的整數儲存在一個array物件，
    # 然後利用tofile()方法寫入檔案
    int_array = arr.array('i', [100, 200, 300])  # 'i'表示資料是整數
    int_array.tofile(output_file)

    # 把要寫入的浮點數儲存在一個array物件，
    # 然後利用tofile()方法寫入檔案
    float_array = arr.array('d', [3.14, 2.7])  # 'd'表示資料是浮點數
    float_array.tofile(output_file)