t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i, j = 0, 0
    turn = 0  # 0 for Bea (1), 1 for Ver (2)

    while True:
        if turn == 0:
            # Bea attacks Ver
            b[j] -= 1
            if b[j] == 0 and j == m - 1:
                print("1")
                break
            if j + 1 < m and b[j + 1] > b[j]:
                j += 1
            turn = 1
        else:
            # Ver attacks Bea
            a[i] -= 1
            if a[i] == 0 and i == n - 1:
                print("2")
                break
            if i + 1 < n and a[i + 1] > a[i]:
                i += 1
            turn = 0