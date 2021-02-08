"""add the digits of a positive integer repeatedly until the result has a single digit."""

def repeat(n):
## ONE LINER
# return (num - 1) % 9 + 1 if num > 0 else 0 

    dig=[]
    Sum = 0
    while n>0:
        dig.append(n%10)
        n = n//10
    Sum = sum(dig)
    return Sum if Sum//10==0 else repeat(Sum)
        
print(repeat(int(input())),end='')
