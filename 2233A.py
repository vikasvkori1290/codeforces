t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    #with ai
    n=a[0]
    x=a[1]
    y=a[2]
    z=a[3]
    totalhours=0
    lineofcode=0
    for i in range(z):
        lineofcode+=x
        totalhours+=1
        if lineofcode >= n:
            break
    while True:
        lineofcode=lineofcode+(x+10*y)
        totalhours+=1
        if lineofcode>=n:
            break

    #without ai
    totalhrs=0
    code=0
    while True:
        code=code+(x+y)
        totalhrs+=1
        if code>=n:
            break
    print(min(totalhours,totalhrs))
        

