t=int(input())
for i in range(t):
    n,w=map(int,input().split())
    if w==1:
        print("0")
    else:
        ans=n-(n//w)
        print(ans)