import collections
from collections.abc import Iterator, Iterable
a = [1, 2]
print(isinstance(a, Iterable)) # True
print(isinstance(a, Iterator)) # False

iter_a = iter(a)
print(isinstance(iter_a, Iterator)) # True
