t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    s=a+b+c
    for k in [3,4,5,6]:
        if s % k == 0:
            x=s//k
            if a%x==0 and b%x==0 and c%x==0:
                print("YES")
                break
    else:
        print("NO")