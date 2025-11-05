#  == type()和instance() 的区别

class A:
    pass

class B(A): pass


a = A()
b = B()

print("=== 示例 1: type() vs isinstance() ===")
print("type(a) is A:", type(a) is A) # True
print("type(b) is A:", type(b) is A) # False b的实际类型是B
print("isinstance(b, A):", isinstance(b, A))
print("isinstance(a, b):", isinstance(a, B))


print("=== 示例 2: type(x) is / == / = 的区别 ===")
x = 123
print("type(x) is int:", type(x) is int)   # True
print("type(x) == int:", type(x) == int)   # True，一般等价于上面
# print("type(x) = int")  # ❌ SyntaxError: cannot assign to function call

# 用自定义类演示 is vs == 差异
class WeirdType:
    def __eq__(self, other):
        print("== 比较触发了 __eq__")
        return True

obj = WeirdType()
print("type(obj) is WeirdType:", type(obj) is WeirdType)
print("type(obj) == WeirdType:", type(obj) == WeirdType)  # 仍然True，但调用 __eq__ 时可被改写
print()


# ===== 示例 3：为什么类内使用 type(self) 或 self.__class__ =====
print("=== 示例 3: type(self) 在继承下的作用 ===")

class Group:
    def __init__(self, group_name, staffs):
        self.group_name = group_name
        self.staffs = staffs

    def __getitem__(self, item):
        cls = type(self)  # 动态取当前实例的类（支持子类多态）
        if isinstance(item, slice):
            return cls(group_name='user', staffs=self.staffs[item])
        if isinstance(item, int):
            return cls(group_name='user', staffs=[self.staffs[item]])

    def __repr__(self):
        return f"<{type(self).__name__} name={self.group_name} staffs={self.staffs}>"

class SpecialGroup(Group):
    pass

g = SpecialGroup("all", ["alice", "bob", "carol"])
print("原始:", g)

# 用 int 索引
one = g[0]
print("g[0]:", one, "类型:", type(one))

# 用 slice 索引
sub = g[1:]
print("g[1:]:", sub, "类型:", type(sub))
print()


# 如果我们在 Group 内写死类名会怎样？
class BadGroup(Group):
    def __getitem__(self, item):
        if isinstance(item, slice):
            # ⚠️ 写死类名，破坏多态
            return Group(group_name='bad', staffs=self.staffs[item])
        if isinstance(item, int):
            return Group(group_name='bad', staffs=[self.staffs[item]])
        return None


bg = BadGroup("all", ["x", "y", "z"])
print("BadGroup[0]:", bg[0], "类型:", type(bg[0]))  # ❌ 返回 Group，而不是 BadGroup