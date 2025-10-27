

class A:
    def __init__(self):
       print("A")

class B(A):
    def __init__(self):
       print("B")
       # 这是py2的语法
       super(B, self).__int__()

b = B()

