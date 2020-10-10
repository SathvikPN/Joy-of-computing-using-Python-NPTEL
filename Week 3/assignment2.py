A = []
for i in range(1,51):
  A.append(i)

a,b = map(int, input().split())

for i in range(a,b-1): 
  print(A[i])
print(A[b-1],end='') 
