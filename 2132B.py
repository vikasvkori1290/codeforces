t=int(input())
for i in range(t):
    n=int(input())
    ans=[]
    for i in range(1,19):
        d=10**i+1
        if n%d==0:
            ans.append(n//d)
    if len(ans)==0:
        print("0")
    else:

        print(len(ans))
        print(*sorted(ans))