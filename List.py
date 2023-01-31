n = []
a = int(input())
for i in range(a):
    x = int(input())
    n.append(x)
for j in n:
    if (j % 2 )== 0:
        n.remove(j)
for i in n:
    print(i)
