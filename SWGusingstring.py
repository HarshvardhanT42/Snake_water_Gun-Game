import string
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
user = input("1 sanke \n 2 water \n 3 gun\n Enter Your Choise")

score = check(comp, user)

print("you: ",user)
print("computer: ",comp)

if(score == 0):
    print("its draw")
elif(score == -1):
    print("you lose")
else:
    print("you won")
