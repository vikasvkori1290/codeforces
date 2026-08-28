t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    maxi=max(a)
    minn=min(a)
    mid=(maxi+minn)//2
    if mid<s:
        print(abs(maxi-s)+(maxi-minn))
    else:
        print(abs(s-minn)+(maxi-minn))