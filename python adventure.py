import sys
import time
import random
global hp
inv = "nothing"
hp = 100
if hp <= 0:
    print("you died")
    sys.exit()
print("hello ")
time.sleep(1)
print("you have entered the py realm ")
name = input("whats your name traveler ")
print("welcome", name, "!")
location = "start"

print("starting game please wait")
time.sleep(1)
print("...")
print("you are on a mountain")

while True:
    d = input("left of right ")
    d = d.lower()
    if d == "left":
        print("you have entered a cave")
        time.sleep(0.5)
        print("and you see a sword and now take it")
        time.sleep(0.5)
        inv = "sword"
        print("you now have a", inv)

        break
    elif d == "right":
        print("you have fallen in to a pit")
        print("and died")
        sys.exit()
        break

    else:
        print("invalid")

print("as you leave the cave you discover a hostile monster")

a = input("attack? type attack to attack ")

if a == "attack":
    print("you attacked and won but lost 50hp and lost your sword")
    time.sleep(1)
    hp = hp - 50
    inv = "nothing"
    print("you now have a", inv)
    time.sleep(0.5)
    print(hp, "hp")


d = input("do you want to goto the" " village " "or continue in the" " mountain  ")
if d == "village":
    print("you went the village and drink a healing potion ")
    time.sleep(1)
    print("!50hp extra!")
    hp = hp + 50
    print(hp, "hp")
    print("you must solve a maths problem to continue")
elif d == "mountain":
    print("you continue in the mountains and trip and lose 50hp")
    hp = hp - 50
    print("you have ", hp ,"hp")


