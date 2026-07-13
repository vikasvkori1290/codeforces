t=int(input())
for i in range(t):
    n, k = map(int, input().split())
    s=str(input())
    possible=True
    for i in range(k):
        count1=0
        for j in range(i,n,k):
            if s[j]=='1':
                count1+=1
        if count1%2!=0:
            possible=False
            break
    if possible:
        print("YES")
    else:
        print("NO")
