t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())
    l=1
    r=2
    minimalcount=2
    while r<n:
        
        if s[l]==s[r]:
            r+=1
        else:
            minimalcount+=1
            l=r
            r+=1
    if len(s)==3:
        print(2)
    else:
        print(minimalcount)