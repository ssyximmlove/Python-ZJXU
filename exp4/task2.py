import random


def task2():
    times = int(input())
    hits = 0
    for i in range(times):
        x=random.random()
        y=random.random()
        if x**2+y**2<=1:
            hits+=1
    print(4.00*hits/times)

if __name__ == "__main__":
    task2()