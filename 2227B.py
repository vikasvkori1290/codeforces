t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    count = 0

    for i in range(n):
        if s[i] == '(':
            count += 1

    if n % 2 == 0 and count == n // 2:
        print("YES")
    else:
        print("NO")