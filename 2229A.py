t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(max(a)-(max(a)+min(a))//2)