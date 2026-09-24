t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    czero=0
    cone=0
    for i in range(n):
        if a[i]==0:
            czero+=1
        else:
            cone+=1
    if cone>=czero:
        print("Bessie")
    else:
        print("Elsie")