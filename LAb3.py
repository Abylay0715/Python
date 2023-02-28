ex1
def gramma(n):
    g = float(n)*28.3495231
    return g

n = input()
print(gramma(n))
ex2
def cel(n):
    C = (5 / 9) * (float(n) - 32)
    return C
print(cel(input()))
ex3
def solve(head , leg):
    x = leg/2 - head
    y = head - x
    return int(x) , int(y)
print(solve(int(input()) , int(input())))
ex4
def prime(l):
    z = True
    ans = []
    for i in l:
        for j in range(2 , i):
            if i%j == 0:
                break
        else:
            ans.append(i)
    return ans
s = input()
s1 = []
for i in range(len(s)):
    s1.append(int(s[i]))
print(prime(s1))
ex5
import itertools

def permut(l):
    l = (list(itertools.permutations(l)))
    for i in l:
        print(i)
s1 = []
s = input()
for i in range(len(s)):
    s1.append(int(s[i]))
permut(s1)
ex6
s = input().split()
print(*s[::-1])
ex7
def has(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1] == 3:
            return True
    return False
s = input()
s1 = []
for i in range(len(s)):
    s1.append(int(s[i]))
print(has(s1))
ex8
def game(l):
   l2 = []
   for i in l:
       if i == 0 and i == 7:
           l2.append(i)
       k=''.join(l2)
   if '007' == k:
       return True
   else:
       return False
s = input()
s1 = []
for i in range(len(s)):
    s1.append(int(s[i]))
print(game(s1))
ex9
from math import pi
def volume(r):
    v = (4/3)*pi*(r**3)
    return v
r = int(input())
print(volume(r))
ex10
def unique(li):
   ans = []
   for i in li:
       if i not in ans:
           ans.append(i)
   return ans
n = int(input())
li = []
for i in range(n):
    x = int(input())
    li.append(x)
print(*unique(li))
ex11
def pal(s):
    s1 = s
    s2 = s[::-1]
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            return False
    return True
s = input()
print(pal(s))

ex12
def histogram(li):
    for i in li:
        print('*' * i)
n = int(input())
li = [int(input()) for i in range(n)]
histogram(li)
ex13
from random import *
def find_number(k , g):
    cnt = 1
    while (k != g):
        if k < g:
            print('Your guess is too low')
        elif k > g:
            print('Your guess is too high')
        print('Take a guess.')
        k = int(input())
        cnt += 1
    return cnt
s = input('Hello! What is your name?')
print('Well,', s, 'I am thinking of a number between 1 and 20.')
guess = randint(1, 20)
print('Take a guess.')
n = int(input())
print('Good job,' , s, 'You guessed my number in', find_number(n , guess), 'guesses!')

Funchion 2

ex1
Write a function that takes a single movie and returns True if its IMDB score is above 5.5
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def check(mov , s):
    for i in mov:
        if i['name'] == s:
            if i['imdb'] > 5.5:
                return True
            else:
                return False
name = input()
print(check(movies , name))
ex 2
Write a function that returns a sublist of movies with an IMDB score above 5.5.
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def fun(mov):
    ls = []
    for i in mov:
        temp = i
        if temp['imdb'] > 5.5:
            ls.append(temp)
    return ls
ls = fun(movies)
for i in ls:
    print(i)
ex3
Write a function that takes a category name and returns just those movies under that category.
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def cat(mov, name):
    ls = []
    for i in mov:
        if i['category'] == name:
            ls.append(i['name'])
    return ls
name = input()
ls = cat(movies , name)
print(ls)
ex4
Write a function that takes a list of movies and computes the average IMDB score.
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def ave(mov):
    n = 0
    for i in mov:
        n+=i['imdb']
    return n/len(mov)
av = ave(movies)
print(av)
ex5
Write a function that takes a category and computes the average IMDB score.
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def ave(mov , name):
    ls = []
    n = 0
    cnt = 0
    for i in mov:
        if i['category'] == name:
            n+=i['imdb']
            cnt+=1
    return n/cnt
name = input()
av = ave(movies , name)
print(av)

#classes
#classes
#ex1

class stt:
    s = None
    def set(self, s):
        self.s = s
    def get(self, s):
        return self.s.upper()

s = stt()
s.set(input())
print(s.get(input()))

ex2
class Shape:
    def area(self):
        return 0


class square(Shape):
    def __init__(self, l):
        self.l = l
    def area(self):
        return self.l * self.l

lenght = int(input())
figure = square(lenght)
print(figure.area())

ex3
class Shape:
    def __init__(self, l, w):
        self.l = l
        self.w = w
class Rectangle(Shape):

    def get(self):
        return self.l * self.w
l , w = int(input()) , int(input())
fig = Rectangle(l , w)

print(fig.get())
ex4
class Point:
    r = None
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x , self.y)
    def move(self , x , y):
        self.x += x
        self.y += y
    def dist(self , x ,y):
        r = ((((self.x - x)**2) + ((self.y - y)**2))**0.5)
        return r

coo = Point(int(input()) , int(input()))
coo.show()
x , y = int(input()), int(input())
coo.move(x , y)
print(coo.dist(x , y))
ex5
class Account:
    owner = None
    balance = None

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        print(f'Account owner:{self.owner} Account balance :{self.balance}')

    def deposit(self, deposit1):
        self.balance += deposit1
        print('Add in deposit')
    def withdraw(self, withd):
        if self.balance >= withd:
            self.balance -= withd
            print('Withdrawal accepted')
        else:
            print('Doesnt have such money')

x = input() #owner name
y = int(input()) #First ballanse
acc1 = Account(x , y)
acc1.__str__()
x1 = int(input()) # add money
acc1.deposit(x1)
x2 = int(input()) # take out from deposit
acc1.withdraw(x2)
ex6
def a(n):
    for j in range(2 , n):
        if n%j == 0:
            return False

    return True

n = [int(input()) for _ in range(int(input()))]
ans = []
for i in n:
    if i == 0 or i == 1:
        continue
    elif a(i) == False:
        continue
    else:
        ans.append(i)

print(ans)





