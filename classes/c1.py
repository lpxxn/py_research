# -*- coding: utf-8 -*-
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float # → 隐式生成 __init__(self, lat: float, ...)

    def __str__(self):
        ns = 'N' if self.lat >=0 else 'S'
        we = 'E' if self.lon >=0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

### 等价于自动创建了以下实现
# class Coordinate(tuple):
#     __slots__ = ()
#     _fields = ('lat', 'lon')
#
#     def __new__(cls, lat: float, lon: float):
#         return tuple.__new__(cls, (lat, lon))
### 现在推荐用 NamedTuple
# 基本理念
#      │
#      ├─ collections.namedtuple (Python 2.6+)
#      │    ├── 工厂函数创建类
#      │    ├── 基于纯元组实现
#      │    └── 无原生类型注解支持
#      │
#      └─ typing.NamedTuple (Python 3.6+)
#           ├── 类继承创建
#           ├── 集成数据类特性
#           └── 完整类型注解支持


beijing = Coordinate(39.9, 116.3)
print(beijing)

point = Coordinate(lat=10, lon=20)

from collections import namedtuple
Point = namedtuple('Point', 'a b')
point = Point(1, b=2)
print(point.a)