t=int(input())
for i in range(t):
    n=int(input())
    y,r=map(int,input().split())
    ans=(y//2)+r
    if ans>n:
        print(n)
    else:
        print(ans)