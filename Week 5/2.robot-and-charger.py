from math import sqrt, floor

directions = {'UP':1, 'DOWN':-1, 'LEFT':-1, 'RIGHT':1}

n = int(input())

x,y = 0,0

for _ in range(n):
  k,v = input().split()
  v = int(v)
  if k in ['LEFT','RIGHT']:
    x += (directions[k]*v)
  else:
    y += (directions[k]*v)
  
print(round(sqrt(x*x+y*y)), end='')
