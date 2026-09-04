t=int(input())
for i in range(t):
    n,k = map(int, input().split())
    s=str(input())
    zeros = s.count('0')
    ones = s.count('1')
    bad=(n//2)-k
    istrue=False
    if zeros>=bad and ones>= bad:
        if (zeros-bad)%2==0:
            istrue=True
    if istrue:
        print("YES")
    else:
        print("NO")