t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    a = []
    d = []
    b = []
    c = []

    for x in arr:
        if x % 6 == 0:
            a.append(x)
        elif x % 2 == 0:
            b.append(x)
        elif x % 3 == 0:
            c.append(x)
        else:
            d.append(x)

    print(*(a + b+ d + c))