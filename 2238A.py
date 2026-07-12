t=int(input())
for i in range(t):
    nc=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    n=nc[0]
    c=nc[1]
    isTrue=True
    cost1=0
    # without reorder
    for i in range(n):
        if a[i] >= b[i]:
            cost1+=a[i]-b[i]
        else:
            cost1=-1
            break
    #with reorder
    a.sort()
    b.sort()
    cost2=c
    for i in range(n):
        if a[i] >= b[i]:
            cost2+=a[i]-b[i]
        else:
            cost2=-1
            break

    if cost1==-1:
        print(cost2)
    elif cost2==-1:
        print(cost1)
    else:
        print(min(cost1,cost2))