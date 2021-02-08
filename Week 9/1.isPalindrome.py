def isPalindrome(txt):
    left,right = 0, len(txt)-1
    while left<=right:
        if txt[left]!=txt[right]:
            return 'NO'
        left +=1
        right -=1
    return 'YES'

if __name__=='__main__':
    txt = input()
    print(isPalindrome(txt))
