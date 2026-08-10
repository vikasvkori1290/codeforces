t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]==67:
            print("YES")
            break
    else:
        print("NO")