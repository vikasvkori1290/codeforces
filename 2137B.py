t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    ans=[]
    for i in range(len(a)):
        ans.append(n+1-a[i])
    print(*ans)