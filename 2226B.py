import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(n - 1):
        diff = abs(a[i] - a[i + 1])
        g = math.gcd(a[i], a[i + 1])

        if diff == g:
            ans += 1

    print(ans)