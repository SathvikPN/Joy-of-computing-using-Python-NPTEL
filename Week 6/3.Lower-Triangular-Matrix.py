def lower_triangle_matrix(n):
    """ Upper triangle all zero"""
    mat = [[int(x) for x in input().split()] for _ in range(n)]

    for row in range(n):
        for i in range(1,n-row):
            mat[row][row+i]=0
    for row in mat:
        print(*row)
    return 'Done...'
        
if __name__=="__main__":
    n = int(input()) # square matrix dimension
    print(lower_triangle_matrix(n))
