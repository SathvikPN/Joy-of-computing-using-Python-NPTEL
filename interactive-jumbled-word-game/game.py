print('''
Jumbled Words Game [2 Player]
''')

import random
import string

#Reading each line(contains a word) from words.txt
f = open('words.txt', 'r')
lines = f.read().splitlines()
words = lines


def agree(n):
    while(n<1):
        n = int(input("No. Rounds: "))
    ans = input('''Both Agree?[1]Yes [2]No
Your choice: ''')
    if(ans!='1'):
        agree(0)
    return n

def shuffle_letters(word):
    word = list(word)
    random.shuffle(word)
    print(word)
    jumbledWord=''.join(word)
    print(jumbledWord)
    
    



rounds = agree(0)
print("*"*50)
print("Game Begins...[Total Rounds: {}]".format(rounds))


word = random.choice(words)
print(word)
shuffle_letters(word)


