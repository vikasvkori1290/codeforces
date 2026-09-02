t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())

    if b * n <= a or b == a:
        print(1)
    else:
        print(2)