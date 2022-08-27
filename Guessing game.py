#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
guess=random.randint(1, 9)#generating a random interger.
print(guess)
number=int(input("Guess a number: "))

if number==guess:
    print("Exactly right ")
elif number>guess:
    print("too high")
elif number<guess:
    print("too low")
else:
    pass