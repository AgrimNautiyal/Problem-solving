def power(n, r):
    if r == 0:
        return 1
    if r%2 == 0:
        step = power(n, r//2) % (1000000007)
        return step*step
    else:
        return (n*(power(n, r-1)%(1000000007)))%(1000000007)

t=int(input())
for i in range(t):
    n = input()
    r = int(''.join(map(str, (list(n)[::-1]))))
    n = int(n)
    
    #to calculate n power n
    res = power(n, r) % (1000000007)
    print(res)
