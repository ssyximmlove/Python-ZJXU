import math
def task5():
    x = input("输入两边之长及夹角: ")
    a,b,theta = map(float,x.split())
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))
    print(c)
if __name__ == "__main__":
    task5()