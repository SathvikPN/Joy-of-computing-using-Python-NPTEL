def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j==n:
                print(j,end='')
            elif j==i:
                print(j)
            else:
                print(j,end=' ')

if __name__ == "__main__":
    rows = int(input()) 
    pattern(rows)
