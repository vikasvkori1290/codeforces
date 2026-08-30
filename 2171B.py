t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    if a[0]==-1 and a[-1]==-1:
        a[0]=0
        a[-1]=0
    elif a[0]==-1:
        a[0]=a[-1]
    elif a[-1]==-1:
        a[-1]=a[0]
    for i in range(1,n-1):
        if a[i]==-1:
            a[i]=0
    for i in range(1,n-1):
        b.append(a[i+1]-a[i])
    ans=abs(sum(b))
    print(ans)
    print(*a)