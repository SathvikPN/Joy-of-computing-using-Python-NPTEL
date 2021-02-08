def pushZero(alist):
    blist = [x for x in alist if x!=0]
    zeros = len(alist)-len(blist)
    blist.extend([0 for _ in range(zeros)])
    print(*blist)
    del blist
    return None

if __name__=='__main__':
    alist = list(map(int,input().split()))
    pushZero(alist)
