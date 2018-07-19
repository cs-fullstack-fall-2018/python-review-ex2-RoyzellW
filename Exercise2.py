import random
randomNumber = random.randint(0,9)
print(randomNumber)




randomNumber = random.randint(0,9)

guess = int(input("Enter a number between 0 and 9: "))

if (guess != randomNumber):
    print(guess)
    print("The correct number was: ", randomNumber)




randomNumber = random.randint(0,9)

guess = int(input("Enter a number between 0 and 9: "))

while (guess != randomNumber):
    print(guess)
    guess = int(input("Enter a number between 0 and 9: "))



randomNumber = random.randint(0,9)

guess = int(input("Enter a number between 0 and 9: "))

while (guess != randomNumber):
    guess = int(input("Enter a number between 0 and 9: "))
    if (guess < randomNumber):
        print("Higher")
    elif(guess > randomNumber):
        print("Lower")
    elif(guess == randomNumber):
        print("You Win!")
