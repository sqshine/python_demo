#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print absolute value of an integer

# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)
# print(r"""hello,\n
# world""")

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# height = 1.75
# weight = 80.5
# bmi = 80.5/(1.75*1.75)
# if bmi < 18.5:
#     print('too thin')
# elif 18.5 < bmi < 25:
#     print('normal')
# elif 25 < bmi < 38:
#     print('little heavy')
# else:
#     print('heavy')
# d = {'a': 1, 'b': 2, 'c': 3}
# for value in d.values():
#     print(value)
#  for k, v in d.items():
#     print(k)
#     print(v)

# from collections import Iterable
#
#
# def g():
#     yield 1
#     yield 2
#     yield 3
#
#
# print('Iterable? g():', isinstance(g(), Iterable))

# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n + p for m in 'XYZ' for n in 'ABC' for p in '123'])

# import os
#
# print(os.listdir('.'))
# print([d for d in os.listdir('.')])


# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# print(d.items())

# print([k + '=' + v for k, v in d.items()])

# L = ['Hello', 'World', 18, 'Apple', None]
# a = [s.lower() for s in L if isinstance(s, str)]

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
#
# for x in fib(5):
#     print(x)


# def is_odd(n):
#     return n % 2 == 1
#
#
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#
#
# def not_empty(s):
#     return s and s.strip()
#
#
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax += n
#     return ax
#
#
# ls = [1, 2, 2, 8, 9.2]
#
# print(calc_sum(*ls))

# def lazy_sum(*args):
#     def calc_sum():
#         ax = 0
#         for n in args:
#             ax += n
#         return ax
#
#     return calc_sum
#
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f())
# print(lazy_sum(1, 3, 5, 7, 9)())


# a = list(filter(lambda n: n % 2 == 1, range(1, 20)))

# import functools
#
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper
#
#
# @log
# def now():
#     print()
#
#
# print(now)
#
# len()


# from enum import Enum, unique
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(Month.Jan)
# Animal = Enum('Animal', 'ANT BEE CAT DOG')
# print(Animal.ANT.value)
#
#
# @unique
# class Weekday(Enum):
#     Sun = 0  # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
#
# print(Weekday.Tue.value)

# try:
#     print('try')
#     r = 1 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally')
# print('end')

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()