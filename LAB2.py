# Python while loops
# ex1
i = 1
while i < 6:
  print(i)
  i += 1
# ex2
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#Python Lists
#ex1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#ex2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#ex3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#ex4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#ex5
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#ex6
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#Python for loops
#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#ex4
for x in range(6):
  print(x)
#ex 5
for x in range(2, 6):
  print(x)
#ex6
for x in range(2, 30, 3):
  print(x)
#ex7
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#ex8
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#Python Arrays
#ex1
cars = ["Ford", "Volvo", "BMW"]
#ex2
x = len(cars)
#ex3
for x in cars:
  print(x)
#ex4
cars.append("Honda")
#ex4
cars.pop(1)
#ex5
cars.remove("Volvo")


#Pyhton Tuples
#ex1

#Python Sets
#ex1
myset = {"apple", "banana", "cherry"}
#ex2
thisset = {"apple", "banana", "cherry"}
print(thisset)
#ex3
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#ex4
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#ex5
myset = {"apple", "banana", "cherry"}
print(type(myset))
#ex6
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Python Dictionaries
#ex1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#ex2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#ex3
print(len(thisdict))
#ex4
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#ex5
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
