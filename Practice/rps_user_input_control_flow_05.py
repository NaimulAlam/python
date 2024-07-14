# value = input("Please enter a value: \n")
# print(value)
import sys
import random
from enum import Enum

# creted a simple RPS class with Enum which helps to use name/value pairs


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# checking how value pairs give output
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
# sys.exit()


print("")
playerchoice = input(
    "Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Sissors:: \n\n")

# cast the player choice into a integer
player = int(playerchoice)

# apply control flow for user interaction
# logical operators
if player < 1 or player > 3:
    sys.exit("You must enter only 1, 2 or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
# str().replace method used
print("You choose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer choose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You Win!")
elif player == 2 and computer == 1:
    print("🎉 You Win!")
elif player == 3 and computer == 2:
    print("🎉 You Win!")
elif player == computer:
    print("😲 Game is a Draw!!!")
else:
    print("💻 Computer Wins!")
print("")
