t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    current = 1

    for i in range(1, n):
        if s[i] != s[i - 1]:
            current += 1

    ans = current

    for i in range(1, n - 1):
        a = s[i - 1]
        b = s[i]
        c = s[i + 1]

        new_length = current - (a != b) - (b != c) + (a != c)

        ans = min(ans, new_length)

    print(ans)