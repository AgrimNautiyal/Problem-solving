#question url : https://practice.geeksforgeeks.org/problems/anagram/0
t = int(input())
for i in range(t):
    inp = input().split()
    w1, w2 = inp[0], inp[1]
    s1, s2 = set(w1), set(w2)
    if len(s1.intersection(s2))==0 and len(w1)==len(w2):
        print('YES')
    else:
        print('NO')