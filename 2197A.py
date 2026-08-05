t=int(input())
for i in range(t):
    x=int(input())

    def summ(a):
        ans=0
        while a>0:
            ans+=a%10
            a//=10
        return ans

    answer = 0
    for i in range(x,x+82,1):
        if (i - summ(i))==x:
            answer+=1
    print(answer)
