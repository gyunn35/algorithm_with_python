# Basic Syntax of Python
```python
# type is determined at runtime
n = 10
print(type(n))  # int
n = "hello world"
print(type(n))  # str

# multiple assignments
n, m = 0, "hello world"
print(n, m)  # 0 hello world

# increment
n = n + 1
n += 1
# can't do n++

# nil -> None
n = 4
n = None
print(n)  # None

# if statements don't need parentheses or curly braces
n = 1
if n < 2:
    n -= 1
elif n == 2:
    n = None
else:
    n += 1
print(n)  # 0

# || -> or
# && -> and
# multi-line conditions are needed to cover with parentheses
n, m = 10, 20
if n == 10 and m == 20:
    n, m = 20, 10
print(n, m)  # 20 10

# while
n = 0
while n < 5:
    n += 1
print(n)  # 5

# looping with i = 0 to i = 4
for i in range(5):
    print(i)

# looping with i = 2 to i = 5
for i in range(2, 6):
    print(i)

# looping with i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

# division is decimal by default
print(5 / 2)  # 2.5

# round down with double slash
print(5 // 2)  # 2

# round down by default!
print(-3 // 2)  # -2 not -1

# round
print(round(-1.45, 1), round(1.54, 1))  # -1.4 1.5

# round towards zero
print(int(-1.45), int(1.54))  # -1 1

# modulo
print(10 % 3)  # 1

# modulo with negative values
# reference: https://stackoverflow.com/a/67139303/21895254
print(-10 % 3)  # 2

# to be consistent with other language's module
import math

print(math.fmod(-10, 3))  # -1.0

# floor and ceil
print(math.floor(3 / 2))  # 1
print(math.ceil(3 / 2))  # 2
print(math.sqrt(2))  # 1.4142135623730951 == 2^0.5
print(math.pow(2, 3))  # 8.0

# max, min int
print(float("inf"))  # inf
print(float("-inf"))  # -inf

# python numbers are infinite so they never overflow
print(math.pow(2, 200))  # 1.6069380442589903e+60
print(float("inf") < math.pow(2, 200))  # False

# array -> list
arr = [1, 2, 3]
print(arr)  # [1, 2, 3]

# dynamic size so can be used as a stack
arr.append(4)
print(arr)  # [1, 2, 3, 4]
arr.pop()
print(arr)  # [1, 2, 3]

# can insert at middle of list, but its time complexity is O(n)
arr.insert(1, 7)
print(arr)  # [1, 7, 2, 3]

# access
print(arr[0], arr[3])  # 1 3

# initialize list
arr = [1] * 5
print(arr, len(arr))  # [1, 1, 1, 1, 1] 5

# negative index
arr = [1, 2, 3, 4]
print(arr[-1], arr[-2])  # 4 3

# slicing
print(arr[1:3])  # [2, 3]

# unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3
# d, e = [1, 2, 3] -> ValueError: too many values to unpack

# loop through list with values
nums = [1, 2, 3, 4]
for n in nums:
    print(n)

# loop through list with indices and values
for i, n in enumerate(nums):
    print(i, n)

# loop through multiple lists simultaneously with unpacking
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)  # 1 4 to 3 6

# reversing list
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)  # [4, 3, 2, 1]

# sorting list
nums.sort()
print(nums)  # [1, 2, 3, 4]
nums.sort(reverse=True)
print(nums)  # [4, 3, 2, 1]

# custom sort
strs = ["bob", "alice", "kevin", "mark"]
strs.sort(key=lambda x: len(x))
print(strs)  # ["bob", "mark", "alice", "kevin"]

# list comprehesion
nums = [i + i for i in range(5)]
print(nums)  # [0, 2, 4, 6, 8]

# 2D list
nums = [[0] * 4 for i in range(4)]
print(nums)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# strings are similar to list
string = "abcde"
print(string[1:4])  # "bcd"

# but strings are immutable
# str[0] = "A" -> TypeError: 'str' object does not support item assignment

string += "fg"
print(string)  # "abcdefg"

# convertions between int and str
print(int("123") + int("123"))  # 246
print(str(123) + str(123))  # 123123

# python does not prevent using some keywords as names of variables
str = "hello"
int = 123
# print(str(123)) -> 'str' object is not callable
# print(int("hello")) -> 'int' object is not callable

# ascii value of character
print(ord("a"))  # 97
print(ord("A"))  # 65

# join strings with delimeter
strings = ["ab", "cd", "ef"]
print(" ".join(strings))  # ab cd ef

# use deque as queue
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # [1, 2, 3]
queue.popleft()
print(queue)  # [2, 3]
queue.pop()
print(queue)  # [2]

# hashset
hash_set = set()
hash_set.add(1)
hash_set.add(2)
hash_set.add(1)
print(hash_set, len(hash_set))  # {1, 2} 2

# check existence of key
print(1 in hash_set)  # True
print(3 in hash_set)  # False
hash_set.remove(2)
print(2 in hash_set)  # False

# list to set
print(set([1, 2, 3]))  # {1, 2, 3}
hash_set = {i for i in range(5)}
print(hash_set)  # {0, 1, 2, 3, 4}

# hashmap -> dict
hash_map = {}
hash_map["alice"] = 88
hash_map["bob"] = 66
hash_map["alice"] = 77
print(hash_map)  # {'alice': 77, 'bob': 66}

# check existence of key
print("alice" in hash_map)  # True
hash_map.pop("alice")
print("alice" in hash_map)  # False

# initialize dicts
hash_map = {"kevin": 55, "mark": 11}
print(hash_map)  # {'kevin': 55, 'mark': 11}

# dict comprehensive
hash_map = {i: i * 2 for i in range(5)}
print(hash_map)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# loop through dict with keys
for key in hash_map:
    print(key)

# loop through dict with values
for value in hash_map.values():
    print(value)

# tuples are similar with immutable lists
tup = (1, 2, 3)
print(tup, tup[0])  # (1, 2, 3) 1

# so can be used as keys of sets and dicts
hash_set = set()
hash_set.add((1, 2))
print(hash_set)  # {(1, 2)}
hash_map = {(1, 2): 3}
print(hash_map)  # {(1, 2): 3}
# hash_set.add([1,2]) -> TypeError: unhashable type: 'list'

# heaps
import heapq

min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 4)
print(min_heap)  # [2, 3, 4]

# min value is always at index 0
while len(min_heap):
    print(heapq.heappop(min_heap))  # 2 to 4

# if you need to use max heap, attach - each of values and attach - again later
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -4)
print(max_heap)  # [-4, -3, -2]
while len(max_heap):
    print(-1 * heapq.heappop(max_heap))  # 4 to 2

# list to heap
nums = [2, 1, 8, 4, 6]
heapq.heapify(nums)
while len(nums):
    print(heapq.heappop(nums))  # 1 to 8 by ascending order


# functions
def my_func(n, m):
    return n * m


print(my_func(1, 2))  # 2


# nested functions
def outer(a, b):
    c = "c"

    def inner(a, b, c):
        return a + b + c

    return inner(a, b, c)


print(outer("a", "b"))  # abc


# nonlocal in nested function
def double(nums, val):
    def helper():
        for i, n in enumerate(nums):
            nums[i] *= n

        # if you modify val that is in outer scope of helper function without nonlocal declaration, it will not be modified
        nonlocal val
        val *= val

    helper()
    return nums, val


nums = [2, 4]
val = 8
print(double(nums, val))  # ([4, 16] 64)


# class
class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size


my_class = MyClass([1, 2, 3])
print(my_class.getLength())  # 3

```
---
### Reference
- [Python for Coding Interviews - Everything you need to Know](https://www.youtube.com/watch?v=0K_eZGS5NsU)