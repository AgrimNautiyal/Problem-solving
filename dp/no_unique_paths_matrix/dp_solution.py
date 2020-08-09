#code

def calc(m,n):
    count = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        count[i][0]=1
        
    for j in range(m):
        count[0][j] = 1
        
    for i in range(1, n):
        for j in range(1, m):
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[n-1][m-1]

t= int(input())
for i in range(t):
    inp = list(map(int, input().split()))
    m,n = inp[0], inp[1]
    print(calc(n,m))