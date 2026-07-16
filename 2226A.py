t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    foundGreater = False
    addedTrailingOneCost = False
    ans=0
    
    for i in range(n-1, -1, -1):
        if a[i] > 1:
            foundGreater = True
            ans += a[i]
        else:   # a[i] == 1
            if not foundGreater and not addedTrailingOneCost:
                ans += 1
                
                addedTrailingOneCost = True
    print(ans)