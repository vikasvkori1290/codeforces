t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    protect = 0
    l = -1

    for r in range(n):

        if s[r] == '1':

            if l == -1:
                protect += 1

            elif r - l >= k:
                protect += 1

            l = r

    print(protect)