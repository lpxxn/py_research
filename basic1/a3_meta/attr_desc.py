import numbers
from datetime import datetime
'''
数据描述符
同时定义了 __get__ 和 __set__，是数据描述符
当执行 user.age = 20 时，调用 IntField.__set__() 方法
'''


class IntField:
    def __set_name__(self, owner, name):
        print(f'__set_name__ 被调用了！')
        print(f'  owner: {owner}')
        print(f'  name: {name}')
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise TypeError('必须是整数')
        if value < 0:
            raise ValueError('必须 >= 0')
        setattr(instance, self.name, value)

class NoneDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value
'''
只定义了 __get__，是非数据描述符
当执行 user.name = 'Mike' 时，直接写入 user.__dict__['name']
'''

class User: # ← 这一行执行完时，__set_name__ 就被调用了
   age = IntField()
   score = IntField()
   name = NoneDataIntField()

print('========== User begin ==========')
user1 = User()
user2 = User()
user1.age = 20
user2.age = 30
print(user1.age)

print('========== User end ==========')

if __name__ == '__main__':
    user = User()
    user.name = 'Mike'
    user.age = 20
    print(f'user __dict__: {user.__dict__}')
    print(user.age)
    print(getattr(user, 'age'))
    # user.age = -1

"""
user.age的查找顺序
- 如果user是某个类的实例，那么`user.age`（以及等价的`getattr(user,’age’)`）
- 首先调用`__getattribute__`, 如果在`__getattribute__`找不到属性就会抛出`AttributeError`
- 如果类定义了`__getattr__`方法，在抛出`AttributeError`的时候就会调用到`__getattr__`
- 而对于描述符`__get__`的调用，则是发生在`__getattribute__`内部的。

user = User(), 那么user.age 顺序如下：
1. 如果“age”是出现在User或其基类的`__dict__`中，且age是data descriptor，那么调用其`__get__`方法
2. 如果“age”出现在user(对象)的`__dict__`中， 那么直接返回 `obj.__dict__[‘age’]`
3. 如果“age”出现在User(类)或其基类的`__dict__`中
- 如果age是non-data descriptor，那么调用其`__get__`方法
- 返回`__dict__[‘age’]`
4. 如果User有`__getattr__`方法，调用`__getattr__`方法，否则
5. 抛出AttributeError

- 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类.__dict__里的
- 对象.__dict__中存储了一些self.xxx的一些东西
"""
