'''
JOC using Python - NPTEL
Factorial Generator
Week 4
Assignment 2
'''
def Factorial(k):
    if((k==0) or (k==1)):
        return 1
    else:
        fact = 2
        for i in range(3,k+1):
            fact = fact * i
        return fact
k = int(input())
while k<0:
    k = int(input())
print(Factorial(k),end='')
