def Multiplication_table(n,k):
    print("-"*20)
    print("Mulitiplication Table of {}".format(n))    
    for i in range(1,k+1):
        print("{} X {} = {}".format(n,i,n*i))
    print("-"*20)
    
n = int(input("Required Mulitiplication Table for "))
k = 10
Multiplication_table(n,k)

while (True):
        ans = int(input('''Enter your selection.
[1].Change both (Multiplication Table number) and (rows)
[2].Change only rows.
[3].Change only Multiplication Table number.
[4].Quit program.

'''))
        if(ans==1):
            n = int(input("Multiplication Table number "))
            k = int(input("Number of rows required  "))
            Multiplication_table(n,k)
        elif(ans==2):
            k = int(input("Number of rows required  "))
            Multiplication_table(n,k)
        elif(ans==3):
            n = int(input("Multiplication Table number "))
            Multiplication_table(n,k)
        elif(ans==4):
            break
        else:
            print("Please enter valid selection")      

print('''
Thank you for using our service.
Have a good-day.

Program terminated...''')
