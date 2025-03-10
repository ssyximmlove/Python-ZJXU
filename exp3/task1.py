def task1():
    max = int(input("请输入一个大于2的自然数: "))
    lst = list(range(2,max))
    m = int(max**0.5)
    for i,v in enumerate(lst):
        if v > m:
            break
        lst[i+1:] = filter(lambda x: x%v!=0,lst[i+1:])
    print(lst,type(lst))

if __name__ == "__main__":
    task1()