# num = []
# n = int(input())
# for i in range(n):
#     num.append(int(input()))
# result = {}
# for i in num:
#     if i not in result:
#         result[i] = 1
#     else:
#         result[i] += 1
# for k, v in result.items():
#     print(k, '-', v)
# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
# k = info.setdefault('adres' , 'Almaty')
# print(info)
# d = info.pop('city', 'No like this element')
# print(info)
# print(d)
# de = info.popitem()
# print(de)
# print(info)
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
dict3 = dict2.copy()
dict2.update(dict1)
print(dict2)
print(dict3)
for i in dict3.keys():
    if i in dict2.keys():
        dict2[i] = dict3[i]+dict2[i]
result.update(dict2)





