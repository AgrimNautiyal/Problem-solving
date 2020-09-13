#User function Template for python3
cache={}
class Solution:
    def MinSquares(self, n):
        if n<=0:
            return 0
        
        if n in cache :
            return cache[n]
        res=n
        for i in range(1, n+1):
            if i*i > n:
                break
            res = min(res, 1+self.MinSquares(n-i*i))
        cache[n] = res
        return res
