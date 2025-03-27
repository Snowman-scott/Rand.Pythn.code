import random

Secret_number = random.randint(1,100)
print("Welcome to this number guessing game :3 \nYou have to try guess the number \nGood luck :)")
g1 = int(input("Enter your guess: "))
while g1 != Secret_number:
    if g1 > Secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    g1 = int(input("Enter your guess: "))
print("Congratulations you guesses the number correctly :3")
print("The number was: ", Secret_number)