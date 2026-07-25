t=int(input())
for i in range(t):
    n=int(input())
    d = 2
    ans = 1

    while d * d <= n:

        if n % d == 0:
            ans *= d

            while n % d == 0:
                n //= d

        d += 1
    if n>=1:
        ans*=n
    print(ans)