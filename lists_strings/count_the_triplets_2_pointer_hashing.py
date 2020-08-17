#question url : https://practice.geeksforgeeks.org/problems/count-the-triplets/0

t= int(input())
for i in range(t):
    n=int(input())
    inp = sorted(list(map(int, input().split())))
    count = 0
    s = set(inp)
    for i in range(n-1):
        for j in range(i+1, n-1):
            target = inp[i] + inp[j]
            if target in s:
                count+=1
    
    if count : print(count)
    else: print(-1)
            