#ex1
# import re
# s = input()
# result = re.findall(r'ab*', s)
# print(result)
#ex2
# import re
#
# s = input()
# result = re.findall(r'ab{2,3}', s)
# print(result)

#ex3
# import re
# s = input()
# result = re.findall(r'[a-z]{1}_[a-z]{1}', s)
# print(result)
#ex4
# import re
# s = input()
# patter = r'[A-Z][a-z]+'
# result = re.findall(patter, s)
# print(result)
#ex5
# import re
# s = input()
# result = re.findall(r'a\w*b', s)
# print(result)
#ex6
# import re
# s = input()
# result = re.sub('[ ,.]', ':', s)
# print(result)
#ex7
#snake case to camal case
#sds_sds_sdsa to SdsSdsSdsa
# import re
# ls = []
# s = input()
# camel = re.split('_', s)
# for i in camel:
#     ls.append(i.capitalize())
#
# camel_case = "".join(ls)
# print(camel_case)
#ex8
# import re
# s = input()
# result = re.split('[A-Z]', s)
# print(result)
#ex9
# import re
# s = input()
# result = re.findall(r'[A-Z][a-z]*', s)
# print(result)
# for i in result:
#     print(i, end=' ')
#ex10
#camel case to snake case
#HelloMyName to hello_my_name_
# import re
# s = input()
# result = re.findall(r'[A-Z][a-z]*', s)
# print(result)
# for i in result:
#     x = i.lower()
#     print(x, end='_')