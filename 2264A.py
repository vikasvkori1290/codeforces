t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    misplaced_indices = [i for i in range(n) if a[i] != i + 1]
        
    if not misplaced_indices:
        print("YES")
    else:
        p_mod = list(a)
        m = len(misplaced_indices)
        for j in range(m):
            p_mod[misplaced_indices[j]] = a[misplaced_indices[m - 1 - j]]
        is_sorted = all(p_mod[i] == i + 1 for i in range(n))
        if is_sorted:
            print("YES")
        else:
            print("NO")
