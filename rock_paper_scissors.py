# start the game
# Ask a player to make a move (r , p , s)
# pc selecrt randomly
# pc == user => Tie
# (user == p and pc == r) or (user == r and pc == s) or (user == s and pc ==p ) 
# user win!
# any case user Lose!
# new game again

import random

while True:

    user = input("Please choose 'r' ='rock' , 's' = 'scissors' , 'p' = 'paper'  \n user : " ).lower()

    pc = random.choice(['s' , 'p' , 'r'])

    print (f" PC   : {pc}")

    if (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc =='p' ) :
        print("User is win!!")

    elif (pc == user):
        print("Tie")
    else:
        print("PC Win!")