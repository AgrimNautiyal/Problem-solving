#question url : https://practice.geeksforgeeks.org/problems/anagram/0
#code
t = int(input())
for i in range(t):
    inp = input().split()
    w1, w2 = inp[0], inp[1]
    s1, s2 = set(w1), set(w2)
    if len(s1)==len(s2) and len(s1) == len(s1.intersection(s2)):
        s={}
        flag = 1
        for i in s1:
            s[i] = w1.count(i)
        for i in s2:
            if s[i]!=w2.count(i):
                flag = -1
                break
        if flag == 1:
            print('YES')
        else:
            print("NO")
    else:
        print("NO")
