#question url : https://practice.geeksforgeeks.org/problems/number-of-pairs/0/
t = int(input())

for i in range(t):
    inp1 = list(map( int , input().split()))
    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())))
    count = 0
    for i in range(inp1[0]):
        for j in range(i, inp1[1]):
            
                if pow(arr1[i], arr2[j]) > pow(arr2[j], arr1[i]):
                    #print(arr1[i],  arr2[j])
                    count+=1
                    
    print(count)