#question url -  https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
#knapsack problem using recursion
def func(vals, wts, idx, w):
    if idx == -1 or w==0:
        return 0
    else:  
        if wts[idx] <= w:
            return max((vals[idx] + func(vals, wts, idx-1, w-wts[idx])), func(vals, wts, idx-1, w))
        else:
            return func(vals, wts, idx-1, w)
    
t = int(input())
for i in range(t):
    n = int(input())
    w = int(input())
    vals = list(map(int, input().split()))
    wts = list(map(int, input().split()))
    
    print(func(vals, wts, n-1, w))