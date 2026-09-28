t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    counto = a.count(1)
    
    if n == 2:
        if a[0] == 0 and a[1] == 0:
            print(0)
        else:
            print(-1)
        continue  # Skip the rest of the loop for n == 2
        
    if a[0] == 0 and a[-1] == 0:
        print(0)
    elif a[0] == 1 and a[-1] == 0:
        print(1 if counto >= 1 else -1)
    elif a[0] == 0 and a[-1] == 1:
        print(1 if counto >= 1 else -1)
    else:
        print(2 if counto >= 2 else -1)