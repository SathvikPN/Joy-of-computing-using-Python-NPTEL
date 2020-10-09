'''
Interactive Calculator
author: Sathvik PN
'''

#Print Instructions about Input
print('''I'm "Calculator"

I perform these operations:
Add[+]  Subtract[-]   Multiply[*]   Divide[/]

Sample Expression input format: 
a+b 
[only two operands a,b which are real positive numbers]
''')


def feedCalculator(operator,a,b):
    if(operator=='+'):
        return a+b
    elif(operator=='-'):
        return a-b
    elif(operator=='*'):
        return a*b
    elif(operator=='/'):
         if(b==0):
             return ("Undefined [Divide by zero error]")
         else:
             return a/b
    else:
        print("Invalid operator")


#Interactive Mode
while(True):
    print('''
Enter the expression [press 'Q' to exit calculator]''')
    
    rawInput = input("Feed ")

    #Stop Interactive mode --> Exit
    if ((rawInput=='q')or(rawInput=='Q')):
        print("-"*50)
        break

    #Checking for Mathematical Operator
    for i in rawInput:
        if (i=='+'):
            #splitting input into 2 items [a,b]
            expression = list(rawInput.split('+'))

            #preserving the operator
            operator = i

            #expression needs only one operator
            break 
        
        elif(i=='-'):
            expression = list(rawInput.split('-'))
            operator = i
            break
        elif(i=='*'):
            expression = list(rawInput.split('*'))
            operator = i
            break
        elif(i=='/'):
            expression = list(rawInput.split('/'))
            operator = i
            break
        
    a = float(expression[0])
    b = float(expression[1])
    print("-"*50)
    print("{}{}{} = {}".format(a,operator,b,feedCalculator(operator,a,b)))
    print("-"*50)
print('''
Thanks for using the service.
Have a good-day.
[Calculator turning OFF...]
Program terminated.''')
    
