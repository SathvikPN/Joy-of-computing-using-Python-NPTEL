def remove_duplicate(alist):
    unique = []
    for x in alist:
        if x not in unique:
            unique.append(x)
    print(*unique)

if __name__ == "__main__":
    alist = list(map(int,input().split()))
    remove_duplicate(alist)
