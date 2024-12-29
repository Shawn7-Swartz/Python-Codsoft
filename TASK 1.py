# ROCK PAPER AND SCISSORS GAME !!

import random

a=0
b=0
x=0
l1=["rock","paper","scissor"]
while x<=5:
    n=input("Enter your choice Rock, paper or Scissors:")
    m=random.choice(l1)
    print("Opponnents choice is",m)

    if n=="rock"and m=="rock" or n=="paper" and m=="paper" or n=="scissor" and m=="scissor" :
        print("Tie")
    elif n=="rock" and m=="paper":
        print("user WINS")
        a+=1
    elif n=="paper" and m=="scissor":
        print("user LOOSE")
        b+=1
    elif n=="scissor" and m=="rock":
        print("user LOOSE")
        b+=1
    else:
        print("user WINS")
        a+=1
        
    x+=1
if a>b:
    print("You Wins")
else:
    print("Computer wins")
    