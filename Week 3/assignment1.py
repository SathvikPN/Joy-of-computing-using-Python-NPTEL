#average
def average(a):
  sum = 0
  n = len(a)
  for i in range(n):
    sum = sum + a[i]
  return (sum/n)

n = 5
a = []
for i in range(n):
  x = int(input())
  a.append(x)
print(average(a),end='')
