#https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

t= int(input())
for i in range(t):
    n = int(input())
    inp = list(map(str, input().split()))
    arr1 = ['0' for i in range(inp.count('0'))]
    arr2 = ['1' for i in range(inp.count('1'))]
    arr3 = ['2' for i in range(inp.count('2'))]
    
    #above takes 3*N complexity - which is still linear
    
    print(' '.join(map(str, arr1+arr2+arr3)))
    