def printDict():
  n = int(input())

  ans = {x:x**2 for x in range(1,n+1)}

  print(ans, end='')

printDict()
