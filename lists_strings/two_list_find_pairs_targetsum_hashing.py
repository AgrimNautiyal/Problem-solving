#question url  : https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x/0
#hashing based question only
t=int(input())

for i in range(t):
    target = list(map(int, input().split()))[-1]
    a1 = sorted(list(map(int, input().split())))
    a2 = set(list(map(int, input().split())))
    
    res=[]
    flag = -1
    for i in a1:
        if target-i in a2:
            if flag == -1: flag = 1
            res.append(str(i) + " " + str(target-i))
    if flag!=-1:
        print(', '.join(res))
    else:
        print(-1)