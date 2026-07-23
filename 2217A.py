t=int(input())
for i in range(t):
    nk=list(map(int,input().split()))
    a=list(map(int,input().split()))
    n=nk[0]
    k=nk[1]
    summ=sum(a)
    if summ%2==1 or (n*k)%2==0:
        print("YES")
    else:
        
        print("NO")