attempts = 0
import randomnumber
guess = int(input("Guess my number between 1 and 50"))

choice = int(randomnumber.random(0,50))
print(f"{choice}")
while attempts < 5:
    if guess < choice:
        print("The number is higher")
        attempts =+ 1
    elif guess > choice:
        print("The number is lower")
        attempts =+ 1
    else:
        print("Not a valid answer")
if guess == choice:
    print("You guessed the number")
else:
    print(f"The number was {choice}")
















