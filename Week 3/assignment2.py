A = []
for i in range(1,51):
  A.append(i)

a,b = input().split()
a= int(a)
b= int(b)
p = A[a:b].copy()
l = len(p)
for i in range(l-1):
  print(p[i])
print(p[l-1],end='')
