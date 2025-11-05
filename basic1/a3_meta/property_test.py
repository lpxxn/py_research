from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = datetime.now().year - self.birthday.year

    @property
    def age(self):
    # return datetime.now().year - self.birthday.year
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


print(f'in {__file__} file')

if __name__ == '__main__':
    user = User('Mike', date(1990, 1, 1))
    print(f'name: {user.name}, age: {user.age}')
    user.age = 20
    print(f'name: {user.name}, age: {user.age}')
