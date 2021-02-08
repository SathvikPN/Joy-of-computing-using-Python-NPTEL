def isPowerof2(n):
    while n>1:
        if(n%2!=0):
            return False
        n = n/2
    return False if n<=0 else True

if __name__=="__main__":
    n = int(input())
    print(isPowerof2(n))
