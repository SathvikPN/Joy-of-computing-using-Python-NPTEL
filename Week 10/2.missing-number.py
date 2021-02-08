def missing(alist):
    for i in range(1,len(alist)+2):
        if i not in alist:
            return i
    return None

inp = list(map(int, input().split()))
print(missing(inp),end='')
