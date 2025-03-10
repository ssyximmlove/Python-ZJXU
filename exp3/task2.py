def task2():
    max = int(input())
    st = set(range(2,max))
    m = int(max**0.5)+1
    for i,v in range(2,m):
        if i%v!=0:
            st.discard(i)
    print(st,type(st))
if __name__ == "__main__":
    task2()



