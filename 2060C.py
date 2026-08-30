t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    l=0
    r=n-1
    x.sort()
    removecount=0
    while l<r:
        total=x[l]+x[r]
        if total==k:
            removecount+=1
            l+=1
            r-=1
        elif total<k:
            l+=1
        else:
            r-=1
    print(removecount)

