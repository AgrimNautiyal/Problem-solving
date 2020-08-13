#question url : https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array/0
t = int(input())
for i in range(t):
    n = int(input())
    inp = list(map(int, input().split()))
    ideal_sum = 2*sum(set(inp))
    actual_sum = sum(inp)
    
    print(ideal_sum-actual_sum)
           
    