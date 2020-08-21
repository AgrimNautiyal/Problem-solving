#question url : https://practice.geeksforgeeks.org/problems/string-manipulation/0
t = int(input())
for i in range(t):
    n = int(input())
    
    inp = input().split()
    
    stack = []
    
    for i in inp:
        
        if len(stack) == 0:
            stack.append(i)
            
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    print(len(stack))