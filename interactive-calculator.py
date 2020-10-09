'''
Calculator
'''
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

print('''I'm "Calculator"

I perform these operations:
Add[+]  Subtract[-]   Multiply[*]   Divide[/]

Sample Expression input:
a+b where a,b are integers
''')

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
    print(rawInput," = ",feedCalculator(operator,a,b))
    print("-"*25)
print("Calculator turning OFF...")
    
