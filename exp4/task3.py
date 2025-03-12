import random


def task3():
    times = int(input())
    hits = 0
    for i in range(times):
        x = random.random()
        y = random.random()
        if x**2 >= y:
            hits += 1
    print(hits/times)

if __name__ == "__main__":
    task3()
