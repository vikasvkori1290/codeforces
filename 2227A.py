t=int(input())
for i in range(t):
    a = list(map(int, input().split()))
    x=a[0]
    y=a[1]
    if x%2==0 and y%2==0:
        print("YES")
    elif x%2==0 or y%2==0:
        print("YES")
    else:
        print("NO")


