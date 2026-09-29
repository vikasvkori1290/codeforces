import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        s = data[idx+2]
        idx += 3
        
        ans = 0
        for i in range(0, n, k):
            farm = s[i:i+k]
            if '0' not in farm:
                ans += 1
                
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()