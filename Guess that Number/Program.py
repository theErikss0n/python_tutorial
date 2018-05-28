import random

print("-------------------------------------")
print("         Guess The Number App        ")
print("-------------------------------------")
print("\n")


random_int = random.randint(0, 100)

user_number = 101

user_name = input("What is your name?: ")

while random_int != user_number:

    user_number = int(input("Guess a number between 0 and 100"))

    if user_number > random_int:
        print("Sorry {}, your guess of {} is to HIGH".format(user_name, user_number))
    elif user_number < random_int:
        print("Sorry {}, your guess of {} is to LOW".format(user_name, user_number))
    else:
        print("Congrats {}, the number was: {} ".format(user_name, random_int))

print("done")
