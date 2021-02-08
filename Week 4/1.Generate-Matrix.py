# Generate Matrix
def generate_matrix(m,n):
    i = 1
    while i<=(m*n):
        for _ in range(n):
            print(i,end=' ')
            i = i+1
        print()
        
row,column = map(int, input("Row Column (space separated):\n").split())
generate_matrix(row,column)
