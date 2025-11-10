

class Person:
    """
    Person
    """
    name = "person"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name
        print(f"{self.name} is from {self.school_name}")



s1 = Student("MIT")
print(s1.__dict__)
# 也可以赋值
s1.__dict__["age"] = 10
print(f"s1 student age: {s1.age}")

print(Student.__dict__)
print(Person.__dict__)

print(f'dir()比__dict__更完整, 只显示实例属性，没有属性的值')
print(dir(s1))
print(dir(Person))


class A:
    value = {}
    a = []
