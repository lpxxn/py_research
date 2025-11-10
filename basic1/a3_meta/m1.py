


class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        print("args := ", args)
        name, base, namespace = args
        return super().__new__(cls, name, base, namespace, **kwargs)

# metaclass= 不要忘了写
class A(metaclass=MyMeta):
    def __init__(self, x):
        self.x = x
a = A("abc")
if __name__ == '__main__':
    a = A(2)

