t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if b<3*a:
        groups = n // 3
        remaining = n % 3
        print(groups * b + min(remaining * a, b))
    else:
        print(a*n)