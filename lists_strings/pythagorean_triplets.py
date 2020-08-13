#question url : https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0

def binary_search(arr, target):
    start = 0 
    end = len(arr)-1
    while(start<=end):
        mid = (start+end)//2
        if arr[mid] == target:
            return True
            break
        if target>arr[mid]:
            start = mid+1
        if  target < arr[mid]:
            end = mid-1
    return False

t = int(input())
for i in range(t):
    n = int(input())
    flag = 0
    inp = sorted(list(map(int, input().split())))
    for i in range(0, n-2):
        if flag == 1:
            break
        for j in range(i+1, n-1):
            t =pow((inp[i]*inp[i] + inp[j]*inp[j]), 0.5)
            #print(inp[i], inp[j])
            if int(t) - t == 0:
                ele = t
                if binary_search(inp[j+1:n-1], ele):
                #if ele in inp[j+1:n-1]:
                    flag  = 1
                    break
    if flag :
        print("Yes")
    else:
        print("No")