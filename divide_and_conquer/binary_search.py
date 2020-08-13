#Your task is to complete this function
#Function should return integer denoting the index
# indexing is done according to 0
# Left=0 and High=0
def bin_search(A, left, right, k):
    #Code here
    while(left<=right):
        mid = (left+right)//2
        if A[mid] == k:
            return mid
        if k > A[mid]:
            left = mid+1
        if k < A[mid]:
            right = mid-1
    return -1


#{ 
#  Driver Code Starts
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split(' ')))
    x=int(input())
    print (bin_search(arr, 0, n-1, x))
# } Driver Code Ends