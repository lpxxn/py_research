

class A:
    def __init__(self, name):
       print("A")
       self.name = name

class B(A):
    def __init__(self):
       print("B")
       # 这是py2的语法
       #super(B, self).__int__()
       super().__init__("haha")

b = B()

