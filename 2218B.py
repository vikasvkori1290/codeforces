t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    maxi=max(a)
    nsum=0
    for i in range(len(a)):
        nsum+=a[i]
    nsum=-nsum
    nsum=nsum+(2*maxi)
    print(nsum)
