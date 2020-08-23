#question url : https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
#knapsack with memoization 
def func(vals, wts, idx, w, cache):
    if idx == -1 or w==0:
        return 0
    else:  
        key = (idx,w)
        if key in cache:
            return cache[key]
            
        if wts[idx] <= w:
            cache[key] = max((vals[idx] + func(vals, wts, idx-1, w-wts[idx], cache)), func(vals, wts, idx-1, w, cache))
            return cache[key]
        else:
            cache[key] = func(vals, wts, idx-1, w, cache)
            return cache[key]
    
t = int(input())
for i in range(t):
    n = int(input())
    w = int(input())
    vals = list(map(int, input().split()))
    wts = list(map(int, input().split()))
    cache={}
    print(func(vals, wts, n-1, w,cache))