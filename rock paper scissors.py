#Question
#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

import sys#module used to provde functions and variables used to manipulate a system
user1=input("What is your name? ")
user2=input("What is your name? ")
user1_answer=input("%s, do you want to chose rock, paper or scissors? ")
user2_answer=input("%s, do you want to chose rock, paper or scissors? ")
def compare(u1, u2):
    if u1==u2:
        return("It's a tie!")
    elif u1=="rock":
        if u2=="scissors":
            return("Rock wins")
        else:
            return("Paper wins")
    elif u1=="scissors":
        if u2=="paper":
            return("Scissors wins")
        else:
            return("Rock wins")
    elif u1=="paper":
        if u2=="Rock":
            return("paper wins")
        else:
            return("Scissors wins")
    else:
        return("Invalid input! you have not entred either paper, rock or scissors")
    sys.exit()
print(compare(user1_answer, user2_answer))