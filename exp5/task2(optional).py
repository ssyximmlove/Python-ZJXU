import random

def fox_game():
    holes = [0, 0, 0, 0, 0]
    fox_position = random.randint(0, 4)
    holes[fox_position] = 1

    while True:
        guess = int(input("Guess the hole (0-4): "))
        if holes[guess] == 1:
            print("Congratulations! You caught the fox!")
            break
        else:
            print("No fox in this hole. Try again tomorrow.")
            # Move the fox to the adjacent hole
            holes[fox_position] = 0
            if fox_position == 0:
                fox_position = 1
            elif fox_position == 4:
                fox_position = 3
            else:
                fox_position = random.choice([fox_position - 1, fox_position + 1])
            holes[fox_position] = 1

if __name__ == "__main__":
    fox_game()