#question : https://practice.geeksforgeeks.org/problems/count-ways-to-express-n-as-the-sum-of-13-and-4/0
cache={}
def func(n):
    if n==0 or n == 1:
        return 1
    if n<=0:
        return 0
    if n in cache:
        return cache[n]
    cache[n]= (func(n-1)+ func(n-3) + func(n-4))%(pow(10,9)+7)
    return cache[n]
    
t=int(input())
for i in range(t):
    n = int(input())
    print(func(n))
