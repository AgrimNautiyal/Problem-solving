#https://practice.geeksforgeeks.org/problems/easy-string/0
t=int(input())
for i in range(t):
    inp = input().lower() + " "
    if len(inp) == 1:
        print('1'+inp)
    prev = 0
    res=''
    count = 1
    l = len(inp)
    for i in range(1, l):
        if inp[i] == inp[prev]:
            count+=1
            prev = i
        else:
            res += str(count) + str(inp[prev])
            prev = i
            count =1 
    print(res)
    