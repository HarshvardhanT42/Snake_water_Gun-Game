
import random

def check(comp, user):
    if comp == user:
        return 0
    if(comp == "Snake" and user == "Water"):
        return -1
    if(comp == "Water" and user == "Gun"):
        return -1
    if(comp == "Gun" and user == "Snake"):
        return -1

    return 1

foo = ["Snake","Gun","Water"]
comp = random.choice(foo)

user_choise= input("\n1 Sanke \n 2 Water \n 3 Gun\n Enter Your Choise")

if user_choise == "1":
    user = "Snake"
elif user_choise == "2":
    user = "Water"
elif user_choise == "3":
    user = "Gun"
else:
    print("Invalid Input")
    
    
if user:
    score = check(comp, user)
    print("you: ",user)
    print("computer: ",comp)

    if(score == 0):
        print("its draw")
    elif(score == -1):
        print("you lose")
    else:
        print("you won")
