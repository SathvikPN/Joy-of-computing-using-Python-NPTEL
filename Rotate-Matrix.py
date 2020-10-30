def printMatrix(M):
    for rows in M:
        print(*rows)

        
def RotateMatrix(mat):
    if not len(mat):
        return
    '''
    (top,bottom) = (starting,ending) row index
    (left,right) = (starting,ending) column index
    '''

    top,bottom = 0, len(mat)-1
    left,right = 0, len(mat[0])-1

    while top<bottom and left<right:
        print('\n\nOuter loop {} starts...'.format(top+1))
        '''
        store 1st value of next row to replace current row 1st element
        '''
        prev = mat[top+1][left]

        print('-'*100)
        print('shift top row elements 1-step right')
        for i in range(left,right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top = top+1
        printMatrix(mat)
        print('-'*100)

        print('shift rightmost column elements 1-step down')
        for i in range(top,bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
        right = right-1
        printMatrix(mat)
        print('-'*100)

        print('shift bottom row elements 1-step left')
        for i in range(right,left-1,-1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom = bottom-1
        printMatrix(mat)
        print('-'*100)

        print('shift leftmost column element 1-step up')
        for i in range(bottom,top-1,-1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left = left + 1
        printMatrix(mat)
        print('-'*100)
        
    return mat
           
    
size = int(input())
matrix = [list(map(int,input().split())) for x in range(size)]

M = RotateMatrix(matrix)
print("driver code runs")
for rows in M:
    print(*rows)
