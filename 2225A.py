t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    x=a[0]
    y=a[1]
    if y//x>2:
        print("YES")
    else:
        print("NO")