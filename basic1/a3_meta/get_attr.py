from datetime import date


class User:
    def __init__(self, name, birthday, info=None):
        self.name = name
        self.birthday = birthday
        self.info = {} if info is None else info

    def __getattr__(self, item): # 查不到属性的时候，会去__getattr__方法中查找
        return self.info.get(item, None)
        # return self.info[item]
        # return "not found attr"
    # def __getattribute__(self, item): # 这个方法是，所有的属性都会去这个方法中查找
    #     return "body"

if __name__ == '__main__':
    user = User('Mike', date(1990, 1, 1), info={'age': 20})
    print(user.name)
    print(user.age)# 查不到属性的时候，会去__getattr__方法中查找
    print(user.haha)