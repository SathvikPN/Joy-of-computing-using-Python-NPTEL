print('''
Jumbled Words Game [2 Player]
''')

import random
import string

def agree(n):
    while(n<1):
        n = int(input("No. Rounds: "))
    ans = input('''Both Agree?[1]Yes [2]No
Your choice: ''')
    if(ans!='1'):
        agree(0)
    return n



rounds = agree(0)
print("*"*50)
print("Game Begins...[Total Rounds: {}]".format(rounds))




