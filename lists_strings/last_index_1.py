#question url : https://practice.geeksforgeeks.org/problems/last-index-of-1/0
t=int(input())
for i in range(t):
    inp = input()
    idx = -1
    l = len(inp)
    for i in range(l-1, -1, -1):
        if inp[i] == '1':
            idx=i
            break
    print(idx)