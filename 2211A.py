t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n<2:
        print(*a)
    else:
        print(*([2]*n))
        