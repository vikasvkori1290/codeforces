t=int(input())
for i in range(t):
    n,s,x=map(int,input().split())
    a=list(map(int,input().split()))
    currsum=sum(a)
    if s>=currsum and (s-currsum)%x==0:
        print("YES")
    else:
        print("NO")
    