a = [int(n) for n in input().split()]
b = {i for i in a if i!=-1}
for i in range(len(a)):
    if i in b:
        a[i]=i
    else:
        a[i]=-1
print(*a,end='')

'''
Description:

Given a list A of elements of length N, ranging from 0 to N-1. All elements may not be present in the array. If the element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present display -1 at that place.

Input Format:
The first line contains n numbers with each number separated by a space.

Output Format:
Print the elements of the list after the modification.

Example:

Input:
-1 -1 6 1 9 3 2 -1 4 -1

Output:
-1 1 2 3 4 -1 6 -1 -1 9

Explanation:
The modified list contains elements such that A[i] = i.
'''
