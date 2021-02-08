n = int(input())
for x in range(n):
    l = input()
    s = l.upper()
    print(s) if x!=n-1 else print(s,end='')
