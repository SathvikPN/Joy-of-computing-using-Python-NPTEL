m,n = map(int,input().split(','))
ans=[]
if m%2!=0:
    m+=1
for x in range(m,n+2,2):
    y = str(x)
    flag = 0
    for i in y:
        if int(i)%2!=0:
            flag=1
            break
    if flag==0:
        ans.append(int(y))
print(*ans,sep=',',end='')


'''
Description:
Write a program, which will find all such numbers between m and n (both included) such that each digit of the number is an even number.

Input Format:
The first line contains value m and n separated by a comma.

Output Format:
The numbers obtained should be printed in a comma-separated sequence on a single line.

Constraints:
1000<=m<=9000
1000<=n<=9000

input: 1000,2080
output: 2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080
