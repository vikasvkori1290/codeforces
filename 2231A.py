t = int(input())
for _ in range(t):
    n = int(input())
    ans=[]
    current=1
    for i in range(n):
        
        ans.append(current)
        current+=1
        if current%3==0:
            current+=1
    print(*ans)




   