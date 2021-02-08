one_hole = ["A","D","O","P","Q","R"]
two_hole = ["B"]

x = input()

c = 0
for j in x:        
    if(j in one_hole):
        c = c+1
    if(j in two_hole):
        c=c+2
print(c) 
