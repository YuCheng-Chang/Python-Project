class MyClass:
    language='Python'
    def __init__(self,version):
        self.verson=version
print(MyClass.__dict__)
print(MyClass.__name__)
obj=MyClass('3.7')

print(obj)
print((obj.__dict__))