#question url : https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0/

def merge(arr1, arr2):
    l = min(len(arr1), len(arr2))
    res=[]
    c1 = 0
    c2 = 0

    while(c1<l and c2<l):
        if arr1[c1] < arr2[c2]:
            res.append(arr1[c1])
            c1+=1
        else:
            res.append(arr2[c2])
            c2+=1
    #we reach here once the smallest array has been completely exahusted
    #hence next step - to append rest of the array to result

    if c1 == l:
        #this means c1 was the smaller array
        #append c2
        for i in arr2[c2:]:
            res.append(i)
    else:
        for i in arr1[c1:]:
            res.append(i)
    return ' '.join(map(str ,res))
t = int(input())
for i in range(t):
    inp1 = list(map(int, input().split()))
    m, n = inp1[0], inp1[1]
    arr1= list(map(int, input().split()))
    arr2= list(map(int, input().split()))
    print(merge(arr1,arr2))
    
    