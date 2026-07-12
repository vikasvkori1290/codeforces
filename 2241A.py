t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    x=a[0]
    y=a[1]
    if x%y==0:
        print("YES")
    else:
        print("NO")