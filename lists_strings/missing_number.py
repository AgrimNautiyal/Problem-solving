#question url : https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
t=int(input())
for i in range(t):
    n = int(input())
    actual_sum = n*(n+1)//2
    current_sum = sum(list(map(int, input().split())))
    print(actual_sum-current_sum)