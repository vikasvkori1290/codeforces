t=int(input())
for i in range(t):
    n=int(input())
    pal = [0,1,2,3,4,5,6,7,8,9,11,22]
 
    for a in pal:
        if a <= n and (n - a) % 12 == 0:
            print(a, n - a)
            break
    else: 
        print(-1)