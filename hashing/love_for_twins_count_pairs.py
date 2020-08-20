#question url : https://practice.geeksforgeeks.org/problems/love-for-the-twins/0
t=int(input())
for i in range(t):
    n = int(input())
    inp = list(map(int, input().split()))
    
    inp_set = set(inp)
    
    pairs = 0
    
    for i in inp_set:
        pairs+= inp.count(i)//2
    print(pairs*2)