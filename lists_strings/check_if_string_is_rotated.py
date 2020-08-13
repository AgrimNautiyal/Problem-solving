#question url : https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places/0
t=int(input())
for i in range(t):
    a = input()
    b = input()
    
    #either rotate two positions backward or forward
    c1 = b[len(b)-2:] + b[0:len(b)-2]
    c2=b[2:] + b[0:2]
    
    if a == c1 or a==c2:
        print('1')
    else:
        print('0')