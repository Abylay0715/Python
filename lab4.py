# generators
# ex1
# print(*(i**2 for i in range(1 , int(input()))))
# ex2
# print(*(i for i in range(1 , int(input())) if i%2==0))
# ex3
# def genf(n):
#     for i in range(n):
#         if i % 3 == 0 or i % 4 == 0:
#             yield i
#
#
# s = genf(int(input()))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# for i in s:
#     print(i)
# ex4
# def squar(a , b):
#     for i in range(a, b+1):
#         yield i**2
# s = squar(int(input()) , int(input()))
# print(next(s))
# print(next(s))
# for i in s:
#     print(i)
#
# ex5
# def fun(n):
#     for i in range(n, -1, -1):
#         yield i
# s = fun(int(input()))
# for i in s:
#     print(i)
# Date
# ex1
# from math import *
# x = int(input())
# print(radians(x))
# ex2
# from math import *
# h = int(input('Height'))
# a = int(input('Base, first value:'))
# b = int(input('Base, second value:'))
# s = ((a+b)*h)*0.5
# print('Expected Output:', s)
# ex3
# from math import *
# n = int(input('Input number of sides:'))
# a = int(input('Input the length of a side:'))
# p = n * a
# b = (a/(2*(tan(radians(180/n)))))
# s = (p*b)/2
# s = floor(s)
# print('The area of the polygon is:', s)
# ex4
# l = int(input('Length of base:'))
# h = int(input('Height of parallelogram:'))
# print('Expected Output:', l*h)
# Date
# ex 1
# import datetime as d
# d1 = d.datetime.today()
# d1 += d.timedelta(days=-5)
# print((d1))
# ex2
# import datetime as d
# t = d.datetime.today()
# y = t - d.timedelta(days=1)
# tom = t + d.timedelta(days=1)
# print('today', t.date())
# print('yesterday', y.date())
# print('tomorrow', tom.date())
# ex3
# import datetime as d
# #delete microseconds
# t = d.datetime.today()
# print(t)
# t = t.replace(microsecond=0)
# print(t)
# ex4
# import datetime as d
# d1 = d.datetime(year=2023, month=2, day=20)
# d2 = d.datetime(year=2023, month=2, day=19)
# d3 = d1 - d2 #difference between two data
# d4 = d3.total_seconds() * 1000000 #day in second then in microsecond
# print('Difference between two datetimes in micro seconds:', d4)
