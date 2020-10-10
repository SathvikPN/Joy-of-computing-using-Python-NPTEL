'''
Jumble Word Game
Author: Sathvik PN
'''

print('''
Jumbled Words Game (2-Player)
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
Make choice: ''')
    if(ans!='1'):
        agree(0)
    return n

def shuffle_letters(word):
    word = list(word) #Splitting string into list of characters
    random.shuffle(word) #Jumble list characters
    jumbledWord=''.join(word) #converting list back to string
    return jumbledWord

def displayBoard(Round,s1,s2):
    print('*'*60)
    print('''End of the Round-{}
Scoreboard:
[Player1] {} points
[Player2] {} points'''.format(Round,s1,s2))
    print('*'*60)
    
    
#Main Function starts here...
rounds = agree(0)
print('')
print("x"*60)
print("The Game Begins...[Total Rounds = {}]".format(rounds))
print("x"*60)

#Score Initialisation
s1,s2 = 0,0


for Round in range(rounds):
    #Player1 Turn
    word = random.choice(words)
#    print(word)
    print("Jumbled Word: {}".format(shuffle_letters(word)))
    ans = input("[Player1] ")
    if(ans==word):
        print("Perfect!\n")
        s1 = s1 + 1
    else:
        print("Oops! it was [{}]\n".format(word))

    #Player 2 Turn
    word = random.choice(words)
#    print(word)
    print("Jumbled Word: {}".format(shuffle_letters(word)))
    
    ans = input("[Player2] ")
    if(ans==word):
        print("Perfect!\n")
        s2 = s2 + 1
    else:
        print("Oops! it was [{}]\n".format(word))

    displayBoard(Round,s1,s2)


if(s1>s2):
    print('''
[Player1] Wins the game. Congratulations...''')

elif(s1<s2):
    print('''
[Player2] Wins the game. Congratulations...''')

else:
    print('''[[[[[ It was a tie! ]]]]]
''')
