'''
Calculator
'''
print('''I'm "Calculator"

I perform these operations:
Add[+]  Subtract[-]   Multiply[*]   Divide[/]

Sample Expression input:
a+b where a,b are real positive numbers
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



while(True):
    print("\nEnter the expression [press 'Q' to exit calculator]")
    rawInput = input("Feed ")
    if ((rawInput=='q')or(rawInput=='Q')):
        print("-"*50)
        break
    for i in rawInput:
        if (i=='+'):
            expression = list(rawInput.split('+'))
            operator = i
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
    print(rawInput," = ",feedCalculator(operator,a,b))
    print("-"*50)
print("Calculator turning OFF...")
    
