def task2():
    setA = eval(input("Enter a set: "))
    setB = eval(input("Enter another set: "))
    print(setA & setB)
    print(setA | setB)
    print(setA - setB)

if __name__ == "__main__":
    task2()