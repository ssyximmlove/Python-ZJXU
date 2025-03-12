import random

def task4():
    times = int(input())
    hits = 0
    for i in range(times):
        x = random.uniform(-2,2)
        y = random.uniform(-1,1)
        if (x**2/4) + (y**2/1) <= 1:
            hits += 1
    print(f"{8.00 * hits / times}.5f")

if __name__ == "__main__":
    task4()