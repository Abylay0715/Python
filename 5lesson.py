# put your python code here
s = input()
cnt = 0
cnt1 = 0
for i in range(len(s)):
    if s[i] in 'ауоыиэяюёе':
        cnt += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщ':
        cnt1 += 1

print('Количество гласных букв равно', cnt)
print('Количество согласных букв равно', cnt1)


