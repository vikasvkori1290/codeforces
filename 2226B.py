# import math

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     ans = 0

#     for i in range(n - 1):
#         diff = abs(a[i] - a[i + 1])
#         g = math.gcd(a[i], a[i + 1])

#         if diff == g:
#             ans += 1

#     print(ans)

def string(n):
    ans = 1  # 2^0 = 1
    i = 0
    while ans < n:
        i += 1
        ans = 2 ** i
    return i

print(string(100)) 