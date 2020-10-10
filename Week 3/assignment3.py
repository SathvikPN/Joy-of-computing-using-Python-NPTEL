A = []
for i in range(1,51):
  A.append(i)

a= input()
a= int(a)
l = len(A)
count = 0
for i in range(a,l):
  if(A[i]%a==0):
    count = count + 1

print(count,end='')
