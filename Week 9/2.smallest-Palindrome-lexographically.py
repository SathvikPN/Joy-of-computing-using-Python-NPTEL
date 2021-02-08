def makePalindrome(s):
    l = len(s)
    ans = [None]*l # Reduce mulitple resizing overhead
    start,end = 0,l-1

    while start<=end:
        values=[s[start],s[end]]
        
        if s[start]!=s[end] and '.' not in values: #No '.' to compensate palindrome requirement
            return [-1]
        
        elif '.' in values: #'.' needs replacement
            if values.count('.')==1:
                ans[start] = s[end] if s[start]=='.' else s[start]
                ans[end] = s[start] if s[end]=='.' else s[end]
                
            else: #if both are '.'
                ans[start] = 'a'
                ans[end] = 'a'
                
        else: #inherently palindrome characters
            ans[start]=s[start]
            ans[end]=s[end]

        start = start+1
        end = end-1
    return ans

if __name__=='__main__':
    s = input()
    alist = makePalindrome(s)
print(*alist,sep='')
