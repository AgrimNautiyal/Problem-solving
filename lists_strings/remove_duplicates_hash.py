#question url: https://practice.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string/0
t=int(input())
for i in range(t):
    inp= input()
    s = set()
    res=''
    for i in inp:
        if i not in s:
            s.add(i)
            res+=i
    print(res)