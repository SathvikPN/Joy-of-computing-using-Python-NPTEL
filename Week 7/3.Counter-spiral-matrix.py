def counterSpiral(mat,n): #(matrix,size)
    left,right = 0,n-1
    top,bottom = 0,n-1
    while left<=right and top<=bottom:
        #LT -- LB
        for i in range(top,bottom+1):
            print(mat[i][left],end=' ')
        left = left + 1

        #LB -- RB
        for i in range(left,right+1):
            print(mat[bottom][i],end=' ')
        bottom = bottom-1
            
        #BR -- TR
        for i in range(bottom,top-1,-1):
            print(mat[i][right],end=' ')
        right = right - 1

        #TR -- TL
        for i in range(right,left-1,-1):
            print(mat[top][i],end=' ')
        top = top + 1
        
if __name__=="__main__":
    size = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(size)]
    counterSpiral(matrix,size)
