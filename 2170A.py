t = int(input())

for _ in range(t):
    n = int(input())

    ans = 0

    for r in range(n):
        for c in range(n):

            cell = r * n + c + 1
            cost = cell
            if r > 0:
                cost += cell - n

            if r < n - 1:
                cost += cell + n

            if c > 0:
                cost += cell - 1

            if c < n - 1:
                cost += cell + 1

            ans = max(ans, cost)

    print(ans)

    