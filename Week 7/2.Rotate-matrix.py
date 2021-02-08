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
   
        '''
        store 1st value of next row to replace current row 1st element
        '''
        prev = mat[top+1][left]


        for i in range(left,right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top = top+1
     
        for i in range(top,bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
        right = right-1
      


        for i in range(right,left-1,-1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom = bottom-1
       

    
        for i in range(bottom,top-1,-1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left = left + 1
        
        
    return mat
            
    
size = int(input())
matrix = [list(map(int,input().split())) for x in range(size)]

M = RotateMatrix(matrix)

for rows in M:
    print(*rows)
