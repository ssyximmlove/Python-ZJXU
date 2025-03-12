def cni(n,i):
    minni=min(i,n-i)
    result=1
    for j in range(0,minni+1):
        result=result*(n-minni +j )//j
    return result