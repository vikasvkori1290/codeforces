t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    c0 = c1 = c2 = 0

    for x in a:
        if x % 3 == 0:
            c0 += 1
        elif x % 3 == 1:
            c1 += 1
        else:
            c2 += 1

    ans = c0

    pairs = min(c1, c2)
    ans += pairs

    c1 -= pairs
    c2 -= pairs

    ans += c1 // 3
    ans += c2 // 3

    print(ans)