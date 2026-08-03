t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    ok = True

    for i in range(n - 1):
        if (w[i] < w[i + 1]) != (i % 2 == 0):
            ok = False
            break

    if ok:
        print("YES")
    else:
        ok = True
        for i in range(n - 1):
            if (w[i] > w[i + 1]) != (i % 2 == 0):
                ok = False
                break

        print("YES" if ok else "NO")