#climb n stairs jumping 1 or 2 steps at a time

def helper(n, cache):
	if n == 0 or n == 1:
		return 1 
	else:
		if n in cache:
			return cache[n]
		else:
			cache[n] = helper(n-1, cache) + helper(n-2, cache)
			return cache[n]
t=  int(input())
for i in range(t):
	n = int(input())
	cache = {}
	print(helper(n, cache))




