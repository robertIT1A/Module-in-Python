# pick a random number

import random
dice = random.randint(1,6)
print(dice)

tries = 3

while tries != 0:
    pick = int(input("\nEnter your guess number: "))
    tries -= 1
    if pick == dice:
        print("You're guess is correct!")
        print(f"Only took {tries} tries")
        break

    else:
        print("Wrong Guess!")
        print(f"Remaining Tries is {tries}")

print("Out of try")

