import random
secret_number = random.randint(1,100)
attempts = 0
max_attempts = 5 
difficulty = input("Choose difficulty (easy/medium/hard):")
if difficulty == "easy":
    max_attempts += 5
elif difficulty == "medium":
    max_attempts == 5
else:
    max_attempts -=2
while attempts < max_attempts:
    guess = int(input("Guess the number:"))
    attempts += 1 
    if guess == secret_number:
        print("You guessed it!")
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")
else:
    print("No attempts")
    print(f"The number was {secret_number}")
