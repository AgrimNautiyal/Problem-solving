def helper(A,B, i, j, count):
    if i==len(A) or j == len(B):
        return count
     
    if A[i] == B[j]:
        #print(A[i], end="")
        count = helper(A,B, i+1, j+1, count+1)
        l.append(A[i])
    
    count = max(count, helper(A, B, i+1, j, 0), helper(A, B, i, j+1, 0))
    
    return count
    
t = int(input())
for i in range(t):
    lengths = list(map(int, input().split()))
    
    
    inp1 = input()
    inp2 = input()
    
    print(helper(inp1, inp2, 0, 0, 0)
    