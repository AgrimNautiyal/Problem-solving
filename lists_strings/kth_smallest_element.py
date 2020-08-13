#question url : https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
#requires  further optimisation : run time of 1.05 units on gfg editor

t= int(input())
for i in range(t):
    n = int(input())
    inp = sorted(list(map(int, input().split())))
    k=int(input())
    print(inp[k-1])