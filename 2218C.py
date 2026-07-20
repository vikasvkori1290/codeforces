t=int(input())
for i in range(t):
    n=int(input())
    ans=[]
    for i in range(1,n+1):
        ans.append(i)
        ans.append(n + 2*i - 1)
        ans.append(n + 2*i)
    print(*ans)