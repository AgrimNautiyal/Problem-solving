#code

def calc(m, n):
    if m ==1 or n==1:
        return 1
   
    return (calc(m-1, n) + calc(m, n-1))

t= int(input())
for i in range(t):
    inp = list(map(int, input().split()))
    m,n = inp[0], inp[1]
    print(calc(m, n))