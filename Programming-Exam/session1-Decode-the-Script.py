n,m = map(int,input().split())
matrix = []
script = []
for x in range(n):
    matrix.append(input().split())

for r in range(m):
    for i in range(n):
        s = matrix[i][r]
        if s.isalnum():
            script.append(matrix[i][r])
            
print(''.join(script),end='')

'''
Question:
Nandini has a complex matrix script. The matrix script is a N X M grid of strings. It consists of alphanumeric characters and symbols (!,@,#,$,%,&). To decode the script, Nandini needs to read each column and select only the alphanumeric characters and connect them. She reads the column from top to bottom and starts reading from the leftmost column. If there are symbols in the decoded script, then Nandini removes them for better readability. Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers N (rows) and M (columns) respectively. 
The next N lines contain the row elements of the matrix script separated by space.

Output Format

Print the decoded matrix script.
Sample Input:
7 3
T s i
h % x
i  # $
s M #
$ a  &
# t %
i r !
Output:
ThisisMatrix
'''
