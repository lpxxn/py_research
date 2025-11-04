

def add(a, b):
    a += b
    return a


class Company:
    # Python 中一个非常著名、也容易让人困惑的“陷阱”：不要在函数或方法的默认参数中使用可变对象（如列表、字典等）。
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)

if __name__ == '__main__':
    a = 1
    b = 2
    c = add(a, b)
    print(f'a: {a}, b: {b}, c: {c}')
    # 整数 1 是 不可变对象。
    # a += b 对于不可变对象来说，等价于 a = a + b。

    a1 = [1, 2]
    a2 = [3, 4]
    a3 = add(a1, a2)
    print(f'a1: {a1}, a2: {a2}, a3: {a3}')
    # 列表是 可变对象。
    # a += b 对于列表，会调用 list.__iadd__ 方法，直接修改原列表对象的内容（不是创建新列表）。


    com1 = Company('com1', ['tom', 'bob'])
    com1.add('lucy')
    print(com1.staffs)
    print(f'Company defaults: {Company.__init__.__defaults__}')
    com2 = Company('com2')
    com2.add('tom')
    print(com2.staffs)
    print(f'Company defaults: {Company.__init__.__defaults__}')
    com3 = Company('com3')
    com3.add('jerry')
    print(com3.staffs)
    print(com2.staffs is com3.staffs)

    print(f'Company defaults: {Company.__init__.__defaults__}')

# 一、问题的根本原因：默认参数只在定义时计算一次
# 当你写：def __init__(self, name, staffs=[]):
# Python 在函数定义那一刻（加载类时）就执行了这行，把 [] 创建出来放进函数对象的 __defaults__ 属性里。
# 也就是说：
# 	•	这个 [] 不是每次调用 __init__ 时重新建的；
# 	•	它是同一个对象，所有没传参数的调用都复用它。
# print(Company.__init__.__defaults__)
# # 输出: ([],)
# 二、调用时发生了什么（一步步看）com2 = Company('com2')
# 	•	你没有传 staffs；
# 	•	所以 self.staffs = staffs 这句相当于 self.staffs = <同一个默认列表>；
# 	•	com2.staffs 和 Company.__init__.__defaults__[0] 指向同一个列表。
# com2.add('tom') 这修改了那个列表的内容（加了 'tom'），
# 所以打印：print(Company.__init__.__defaults__)
# # 变成 (['tom'],)
# com3 = Company('com3') 又没传 staffs，那自然还是拿同一个列表对象，
# 因此：com3.staffs is com2.staffs  # True

# ❌ 不要用可变对象（list, dict, set）作为默认参数
# ✅ 用 None 作为默认值，在函数内部创建新对象
# 这个规则适用于所有函数，不只是 __init__  v1.py里有详细的例子

#  有问题的写法（有默认值 + 可变对象）如果不写默认值也没有问题 f1(x): x.append(a) return x

print("*"*20)
class Company:
    def __init__(self, name, staffs=None):
        self.name = name
        # None 表示没有传，创建一个新列表
        # 如果传了外部列表，就复制一份，避免共享引用
        self.staffs = [] if staffs is None else list(staffs)

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)

com1 = Company('com1', ['tom', 'bob'])
com1.add('lucy')
print(com1.staffs)
print(Company.__init__.__defaults__)

com2 = Company('com2')
com2.add('tom')
print(com2.staffs)
print(Company.__init__.__defaults__)

com3 = Company('com3')
com3.add('jerry')
print(com3.staffs)
print(com2.staffs is com3.staffs)
print(Company.__init__.__defaults__)