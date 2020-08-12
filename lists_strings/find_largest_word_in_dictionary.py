#code
t=int(input())

for i in range(t):
    n=int(input())
    inp = list(map(str, input().split()))
    s = input()
    
    lengths=''
    
    for i in inp:
        flag = 1
        for j in i :
            if j not in s:
                flag = 0
                break
        if flag :
            if len(i)>len(lengths):
                lengths = i
    print(lengths)
        