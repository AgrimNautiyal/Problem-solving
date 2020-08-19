#question url : https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/0
t = int(input())
for i in range(t):
    n = int(input())
    arr = input().split()
    s = 0
    B=None
    a=0
    #to maintain constant space
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        s+=arr[i]
        a+=(i+1)
    
    arr = set(arr)
    for i in range(1, n+1):
        if i not in arr:
            A = i
            break
    
    diff= s- a
    B = A+diff
    print(B, A)
    
        
    