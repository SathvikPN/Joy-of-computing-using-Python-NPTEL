from math import sqrt 
D = [int(x) for x in input().split(',')]
Q = []
for d in D:
    q=sqrt((2*50*d)/30)
    Q.append(round(q))
print(*Q,sep=',',end='')

'''
Description:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Input Format:
A sequence of values for D with each value separated by a comma.

Output Format:
Print the sequence of Q values with each value separated by a comma.

Example:

Input:
100,150,180

Output:
18,22,24
'''
