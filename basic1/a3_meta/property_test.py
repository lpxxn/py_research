from datetime import  date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):
        return datetime.now().year - self.birthday.year

print(f'in {__file__} file')

if __name__ == '__main__':
    user = User('Mike', date(1990, 1, 1))
    print(f'name: {user.name}, age: {user.age()}')
