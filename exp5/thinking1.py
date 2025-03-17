from random import randint

def guess_game():
    # Generate a random number between 1 and 100
    secret_number = randint(1, 100)
    attempts = 0

    print("Welcome to the guessing game! Try to guess a number between 1 and 100.")

    # Using a while loop to allow unlimited guesses
    guessing = True
    while guessing:
        try:
            # Get user input
            guess = input("Please input a number: ")

            # Convert input to integer
            num = int(guess)
            attempts += 1

            # Compare the guess with the secret number
            if num == secret_number:
                print(f"Congratulations! You are right! It took you {attempts} attempts.")
                guessing = False
            elif num < secret_number:
                print("The number you input is smaller than the answer.")
            else:
                print("The number you input is larger than the answer.")

        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a number.")

    print("Game over!")

if __name__ == "__main__":
    guess_game()