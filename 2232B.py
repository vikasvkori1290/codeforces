t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    currsum = 0
    minimum = float('inf')

    for i in range(1,n)+1:
        currsum += a[i]

        current = currsum // (i)
        minimum = min(minimum, current)

        a[i] = minimum

    print(*a)