def game(l):
    ans = []
    for i in range(len(l)):
        if l[i] == '0':
            for j in range(i ,len(l)):
                if l[j] == '0':
                    for k in range(j , len(l)):
                        if l[k] == '7':
                            return True


    return False
l = []
s = input()
for i in range(len(s)):
    l.append(s[i])
print(game(l))