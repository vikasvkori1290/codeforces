t=int(input())
for i in range(t):
    n = int(input())

    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    freq={}
    for i in range(n):
        for j in range(n):
            value = matrix[i][j]

            if value in freq:
                freq[value] += 1
            else:
                freq[value] = 1
    maxi = max(freq.values())
    if maxi>(n*n)-n:
        print("NO")
    else:
        print("YES")    

