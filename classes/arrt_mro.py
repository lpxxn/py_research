

class D:
    pass
class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(f'A mro is {A.mro()}, mro 返回的是列表[...]')
print(f'A mro is {A.__mro__}, __mro__ 返回的是元组(...)')
