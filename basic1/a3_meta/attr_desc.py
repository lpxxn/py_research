import numbers
from datetime import datetime

class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise TypeError('age must be an integer')
        if value < 0:
            raise ValueError('age must be >= 0')
        self.value = value
    def __delete__(self, instance):
        pass

class User:
   age = IntField()

# class User:
#     def __init__(self, name, email, birthday):
#         self.name = name
#         self.birthday = birthday
#         self.email = email
#         self._age = datetime.now().year - self.birthday.year
#
#     @property
#     def age(self):
#     # return datetime.now().year - self.birthday.year
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age


print(f'in {__file__} file')

if __name__ == '__main__':
    # user = User('Mike', date(1990, 1, 1))
    # print(f'name: {user.name}, age: {user.age}')
    # user.age = 20
    # print(f'name: {user.name}, age: {user.age}')
    user = User()
    user.age = 20
    print(user.age)
    user.age = -1
