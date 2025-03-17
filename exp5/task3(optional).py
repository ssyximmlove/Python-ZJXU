def compare_numbers():
    """
    A program that compares two numbers entered by the user.
    Continues until the user chooses to exit.
    """
    while True:
        try:
            # Prompt the user to input the first number
            num1_input = input("Enter the first number (or type 'exit' to quit): ")

            # Check if the user wants to exit
            if num1_input.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break

            # Convert the input to a float
            num1 = float(num1_input)

            # Prompt the user to input the second number
            num2_input = input("Enter the second number (or type 'exit' to quit): ")

            # Check if the user wants to exit
            if num2_input.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                break

            # Convert the input to a float
            num2 = float(num2_input)

            # Compare the two numbers and display the result
            if num1 > num2:
                print(f"{num1} is greater than {num2}")
            elif num1 < num2:
                print(f"{num1} is less than {num2}")
            else:
                print(f"{num1} is equal to {num2}")

        except ValueError:
            # Handle the case where the input is not a number
            print("Invalid input. Please enter numeric values.")

        except KeyboardInterrupt:
            # Handle the case where the user wants to exit the game with Ctrl+C
            print("\nExiting the game. Goodbye!")
            break

if __name__ == "__main__":
    compare_numbers()