t=int(input())
for i in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    ans = []
    for i in range(n):
        ans.append(grid[0][i])
    for i in range(1, n):
        ans.append(grid[i][n - 1])
    for i in range(1, 2*n + 1):
        if i not in ans:
            ans.insert(0, i)
            break
    print(*ans)