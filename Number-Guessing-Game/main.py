import random

def process_guess(max_chances, secret_number):
    chances = 0
    while chances < max_chances:
        guess = int(input("\nEnter your guess: "))
        chances += 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {chances} attempts.")
            break

        elif guess < secret_number:
            print(f"Incorrect! The number is greater than {guess}.")
        
        elif guess > secret_number:
            print(f"Incorrect the number is less than {guess}.")

def easy():
    print("\nGreat! you have selected the Easy difficulty level.")
    print("Let's start the game!")

    secret_number =  random.randint(1, 100)
    max_chances = 10
    process_guess(max_chances, secret_number)

def medium():
    print("Great! you have selected the Medium difficulty level.")
    print("Let's start the game!")

    secret_number = random.randint(1, 100)
    max_chances = 5
    process_guess(max_chances, secret_number)

def hard():
    print("Great! you have selected the Hard difficulty level.")
    print("Let's start the game!")

    secret_number = random.randint(1, 100)
    max_chances = 3
    process_guess(max_chances, secret_number)

def main():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100 \n")

    print("Please select the difficulty level: \n" \
    "1. Easy (10 chances) \n" \
    "2. Medium (5 chances) \n" \
    "3. Hard (3 chances)\n")

    user_choice = int(input("Enter your choice: "))

    while user_choice in [1, 2, 3]:
        if user_choice == 1:
            easy()
        if user_choice == 2:
            medium()
        if user_choice == 3:
            hard()
    else:
        print("Invalid prompt")

main()