#code
def recursive(A, B, i, j ,count, cache):
    #base case : 
    if i ==len(A) or j == len(B):
        #this means we've reached the end of shortest string
        return count
    key = (i,j)
    if A[i] == B[j] :
        if key in cache:
            return cache[key]
        else: 
            cache[key] = recursive(A, B, i+1, j+1, count+1, cache)
    cache[key] = max(recursive(A,B,i+1,j,count,cache), recursive(A,B,i,j+1,count,cache))       
    return cache[key]

t=int(input())
for i in range(t):
    inp = list(map(int, input().split()))
    i1= input()
    i2 = input()

    print(recursive(i1, i2, 0, 0, 0, {}))
    
