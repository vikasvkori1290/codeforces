from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    p = deque(map(int, input().split()))

    need = 1
    ok = True

    while p:
        if p[0] == need:
            p.popleft()
        elif p[-1] == need:
            p.pop()
        else:
            ok = False
            break
        need += 1

    print("YES" if ok else "NO")