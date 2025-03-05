def task4():
    x = input("Enter a 3-digits-number: ")
    if len(x) != 3:
        print("Invalid input")
        return
    x = int(x)
    a = x // 100
    b = x % 100 // 10
    c = x % 10
    print(x // 100)
    print(x % 100 // 10)
    print(x % 10)

if __name__ == "__main__":
    task4()