t = int(input())

for _ in range(t):
    n, m, d = map(int, input().split())

    maxboxes = (d // m) + 1

    print((n + maxboxes - 1) // maxboxes)