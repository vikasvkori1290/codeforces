t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    codd = 0
    ceven_0 = 0  
    ceven_2 = 0 
    for x in a:
        if x % 2 != 0:
            codd += 1
        elif x % 4 == 0:
            ceven_0 += 1
        else:
            ceven_2 += 1
            
    print(max(codd, ceven_0, ceven_2))