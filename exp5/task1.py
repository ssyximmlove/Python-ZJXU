from random import randint

def guess(times):
    guessRes = randint(1, 100)
    for i in range(0,times):
        num = int(input("Please input a number: "))
        if num == guessRes:
            print("Congratulations! You are right!")
            break
        elif num < guessRes:
            print("The number you input is smaller than the answer,You have {} chances left.".format(times-1-i))
        else:
            print("The number you input is larger than the answer,You have {} chances left.".format(times-1-i))
    print("The answer is: {}".format(guessRes))

if __name__ == "__main__":
    times = int(input("Please input the times you want to guess: "))
    guess(times)