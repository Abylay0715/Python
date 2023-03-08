#python builtin functions exercises
#ex1
# import math
# ls = [1, 2, 3, 4, 5]
# x = math.prod(ls)
# print(x)
#ex2
# s = input()
# cnt= 0
# cnt1 = 0
# for i in range(len(s)):
#     if s[i]>='a' and s[i]<='z':
#         cnt+=1
#     elif s[i]>='A' and s[i]<='Z':
#         cnt1+=1
# print('Number word in lowercase:', cnt, 'Number in uppercase:', cnt1)
#ex3
# def ispal(s):
#     x = list(s)
#     y = []
#     y.extend(x)
#     x.reverse()
#     if x==y:
#         return True
#     return False
# s = input()
# print(ispal(s))
#ex4
# import time
# import math
#
# x = int(input())
# ms = int(input())
# t = math.sqrt(x)
# time.sleep(ms/1000)
# print('Square root of', x, 'after', ms,  'miliseconds is',t)
#ex5
# t = (True, True, True)
# t1 = (True, False, True)
# print(all(t))
# print(all(t1))




#Dir-and-Files
import os
#ex1
# path = r'C:\Users\User\Desktop\python'
#
# print("directories:")
# print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
#
# print('files:')
# print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
#
# print('All directories and files')
# print([name for name in os.listdir(path)])
#ex2
#Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified path
# path = os.getcwd()
# print(path)
# print(os.access(path, os.F_OK)) #existence
# print(os.access(path, os.R_OK)) #readability
# print(os.access(path, os.W_OK)) #writability
# print(os.access(path, os.X_OK)) # executability

#ex3
#Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.

# path = os.getcwd()
# a = os.path.exists(path)
# print(a)
# path2 = r'C:\Users\User\Desktop\c++'
# b = os.path.exists(path2)
# print(b)
# path3 = r'C:\Users\User\Desktop\python\c.txt'
# c = os.path.basename(path3)
# print(c)
# s = os.path.dirname(path)
# print(s)
#ex4
#Write a Python program to count the number of lines in a text file.

# with open ('c.txt','r') as f:
#     c = f.read()
#     g = c.splitlines()
#     print(len(g))
#     print(g)

#ex5
#Write a Python program to write a list to a file.
# ls = ['Abylay', 'KBTU', 'Python']
# with open('ex5.txt', 'w') as f:
#     for a in ls:
#         f.write(f'{a}\n')
#ex6
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# import string
# for i in string.ascii_uppercase:
#     filename = os.path.join(r'C:\Users\User\Desktop\python\ex6', f'{i}.txt')
#     with open(filename, 'w') as f:
#         f.write(f'{i}')

#ex7
#Write a Python program to copy the contents of a file to another file
# with open('ex5.txt') as f1:
#     with open ('c.txt', 'w') as f2:
#         for line in f1:
#             f2.write(line)
#ex8
#Write a Python program to delete file by specified path.
# Before deleting check for access and whether a given path exists or not.
# path = r'C:\Users\User\Desktop\python\ex8'
# if os.path.exists(path):
#     try:
#         os.remove(r'C:\Users\User\Desktop\python\ex8\Del.txt')
#     except FileNotFoundError:
#         print('Файла нету')


