t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if (x - 2*y) % 3 != 0:
        print("NO")

    elif y >= 0 and x >= 2*y:
        print("YES")

    elif y < 0 and x >= -4*y:
        print("YES")

    else:
        print("NO")