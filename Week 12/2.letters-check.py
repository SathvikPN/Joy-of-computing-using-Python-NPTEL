s = input()
uppercases = 0
lowercases = 0
for l in s:
    if l.isupper():
        uppercases+=1
    elif l.islower():
        lowercases+=1
print(uppercases,lowercases,end='')
