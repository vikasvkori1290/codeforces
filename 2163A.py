t=int(input()) 
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    isTrue=True
    for i in range(1,n-1,2):
        if a[i]!=a[i+1]:
            isTrue=False
            break
    if isTrue:
        print("YES")
    else:
        print("NO")
