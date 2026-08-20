t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    z = 0
    x = 0
    ans = 0
    for i in range(len(a)):
        if a[i] == 0:
            z += 1
        elif a[i] == -1:
            x += 1

    if x % 2 == 0:
        print(z)
    else:
        print(z + 2)