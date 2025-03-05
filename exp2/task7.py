import random

def task7():
    list = []
    for i in range(10):
        list.append(random.randint(1, 100))
    list.sort()
    print(list)

if __name__ == "__main__":
    task7()