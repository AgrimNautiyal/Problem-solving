#question : https://practice.geeksforgeeks.org/problems/maximum-sum-problem/0
cache={}
def func(n):
    if n==1 or n==0:
        return n
    if n in cache:
        return cache[n]
        
    cache[n]= max(n, func(n//2)+func(n//3)+func(n//4))
    return cache[n]
    
t=int(input())
for i in range(t):
    n=int(input())
    print(func(n))
