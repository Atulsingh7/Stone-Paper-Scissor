# Stone , Paper , Scissor Game
import random

x1 = int(0)
x2 = int(0)
n=11
print("***** WELCOME *****")
print("You have 10 chances to win this GAME\n")
while(n!=1):
    n=n-1


    print("1. for stone")
    print("2. for paper ")
    print("3. for scissor")

    dict={
        1:"STONE",
        2:"PAPER",
        3:"SCISSOR"
    }

    list=[1,2,3]
    bot=random.choice(list)

    human=int(input())

    if(human==1 and bot==1): # case 1
        print(f"you choose STONE and bot choose {dict[bot]}")
        print("----Draw----")
        print("HUMAN : ",x1)     #x1 and x2 are POINTS
        print("BOT : ",x2)
        print(f"Chances left: {n-1}")
        print("\n")

    elif(human==1 and bot==2):    #case 2
        x2 = x2 + 1
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("----BOT WON----")
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")


    elif (human == 1 and bot == 3):  # case 3
        x1 = x1 + 1
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("----Human WON!!!---- ")
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")


    elif (human == 2 and bot == 1):  # case 4
        x1 = x1 + 1
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("----Human WON---- ")
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")


    elif (human == 2 and bot == 2):  # case 5
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("---- DRAW ----")
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")

    elif (human == 2 and bot == 3):  # case 6
        x2 = x2 + 1
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("----BOT WON---- ")
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")


    elif (human == 3 and bot == 1):  # case 7
        x2 = x2 + 1
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("----BOT WON---- ")
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")

    elif (human == 3 and bot == 2):  # case 8
        x1 = x1 + 1
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("----HUMAN WON---- ")
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")

    else:
        print(f"you choose {dict[human]} and bot choose {dict[bot]}")
        print("----Draw----")               #case 9
        print("HUMAN : ", x1)
        print("BOT : ", x2)
        print(f"Chances left: {n - 1}")
        print("\n")


if(x1>x2):
    print("\n Final Scores")
    print(f"HUMAN : {x1}")
    print(f"BOT : {x2}")
    print("\n *****CONGRATULATIONS YOU WIN*****")

elif(x2>x1):
    print("\n Final Scores")
    print(f"HUMAN : {x1}")
    print(f"BOT : {x2}")
    print("\n *****BOT WINS*****")
    print("Better Luck Next Time.")

else:
    print("\n Final Scores")
    print(f"HUMAN : {x1}")
    print(f"BOT : {x2}")
    print("\n *****MATCH DRAW*****")
    print("PLAY AGAIN TO WIN")


