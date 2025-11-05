# ❌ 错误写法
def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list

# 测试
result1 = add_item('apple')
print(result1)  # ['apple']

result2 = add_item('banana')
print(result2)  # ['apple', 'banana']  ← 🐛 包含了上次的数据！

result3 = add_item('cherry')
print(result3)  # ['apple', 'banana', 'cherry']

print(result1 is result2 is result3)  # True - 都是同一个对象！



def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

result1 = add_item('apple')
print(result1)  # ['apple']

result2 = add_item('banana')
print(result2)  # ['banana']  ← ✅ 独立的列表


# ❌ 看似聪明的"缓存"，实际是陷阱
def process_data(data, cache={}):
    if data in cache:
        print(f"从缓存读取: {data}")
        return cache[data]

    # 模拟复杂计算
    result = data * 2
    cache[data] = result
    print(f"计算并缓存: {data} -> {result}")
    return result


# 测试
print(process_data(5))  # 计算并缓存: 5 -> 10
print(process_data(5))  # 从缓存读取: 5
print(process_data(3))  # 计算并缓存: 3 -> 6

# 查看默认参数
print(f"函数默认参数: {process_data.__defaults__}")


# ({5: 10, 3: 6},)  ← 默认字典被修改了！

# 新的调用会继承之前的"缓存"
def another_usage():
    print(process_data(5))  # 从缓存读取: 5  ← 意外地使用了之前的缓存！
another_usage()


def process_data(data, cache=None):
    if cache is None:
        cache = {}

    if data in cache:
        print(f"从缓存读取: {data}")
        return cache[data]

    result = data * 2
    cache[data] = result
    print(f"计算并缓存: {data} -> {result}")
    return result


