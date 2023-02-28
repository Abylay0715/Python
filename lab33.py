#classes
#ex1

# class stt:
#     s = None
#     def set(self, s):
#         self.s = s
#     def get(self, s):
#         return self.s.upper()
#
# s = stt()
# s.set(input())
# print(s.get(input()))

#ex2
# class Shape:
#     def area(self):
#         return 0
#
#
# class square(Shape):
#     def __init__(self, l):
#         self.l = l
#     def area(self):
#         return self.l * self.l
#
# lenght = int(input())
# figure = square(lenght)
# print(figure.area())

#ex3
# class Shape:
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w
# class Rectangle(Shape):
#
#     def get(self):
#         return self.l * self.w
# l , w = int(input()) , int(input())
# fig = Rectangle(l , w)
#
# print(fig.get())
#ex4
# class Point:
#     r = None
#     def __init__(self, x , y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(self.x , self.y)
#     def move(self , x , y):
#         self.x += x
#         self.y += y
#     def dist(self , x ,y):
#         r = ((((self.x - x)**2) + ((self.y - y)**2))**0.5)
#         return r
#
# coo = Point(int(input()) , int(input()))
# coo.show()
# x , y = int(input()), int(input())
# coo.move(x , y)
# print(coo.dist(x , y))
#ex5
# class Account:
#     owner = None
#     balance = None
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def __str__(self):
#         print(f'Account owner:{self.owner} Account balance :{self.balance}')
#
#     def deposit(self, deposit1):
#         self.balance += deposit1
#         print('Add in deposit')
#     def withdraw(self, withd):
#         if self.balance >= withd:
#             self.balance -= withd
#             print('Withdrawal accepted')
#         else:
#             print('Doesnt have such money')
#
# x = input() #owner name
# y = int(input()) #First ballanse
# acc1 = Account(x , y)
# acc1.__str__()
# x1 = int(input()) # add money
# acc1.deposit(x1)
# x2 = int(input()) # take out from deposit
# acc1.withdraw(x2)
#ex6
# def a(n):
#     for j in range(2 , n):
#         if n%j == 0:
#             return False
#
#     return True
#
# n = [int(input()) for _ in range(int(input()))]
# ans = []
# for i in n:
#     if i == 0 or i == 1:
#         continue
#     elif a(i) == False:
#         continue
#     else:
#         ans.append(i)
#
# print(ans)




