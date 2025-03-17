import random

def task5():
    times = int(input())
    hits = 0
    for i in range(times):
        x = random.uniform(0,2)
        y = random.uniform(0,8)
        if (x**2 +x +2) <= y:
            hits += 1
    print(f"{16.00 * hits / times:.7f}")

if __name__ == "__main__":
    task5()