#question url : https://practice.geeksforgeeks.org/problems/remove-duplicates/0
t=int(input())
for i in range(t):
    new = []
    s={}
    inp = input()
    for i in inp:
        if i not in s:
            s[i] = 1
            new.append(i)
        else:
            continue
    print(''.join(map(str, new)))