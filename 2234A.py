t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    
    possible = True
    for i in range(2, n):
        if a[i] != a[i-2] % a[i-1]:
            possible = False
            break
            
    if possible:
        print(a[0], a[1])
    else:
        print(-1)