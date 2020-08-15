level=3
result={10 : lambda: print('Perfect'),9  : lambda: print('A'),8  : lambda: print('B'),7  : lambda: print('C'),6  : lambda: print('D')}.get(level,lambda:print('E'))
print(result)
result()