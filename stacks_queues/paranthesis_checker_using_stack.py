#question url : https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
t = int(input())
for i in range(t):
    inp = input()
    stack = []
    flag = 1
    for i in inp:
        if i in '[{(':
            #this means that current character is an opening bracket 
            #so we have to simply push to our stack
            stack.append(i)
        else:
            #this means that current character is a closed bracket
            #we are now required to verify if top element of stack
            #is a closed bracket or not and whether it is of the same type
            try:
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{' :
                    stack.pop()
                elif i == ')' and stack[-1] == '(' : 
                    stack.pop()
                else:
                    #in this case the incoming character and the previous 
                    #character are not compatible
                    #so we just return a negative result for flag and exit
                    flag = -1
                    break
            except:
                #this case handles situations in which stack is already
                #empty and we are trying to look at a closed character
                #which is an illegal situation so we directly return -1 and exit
                flag = -1
    if len(stack) == 0 and flag == 1:
        #in this case the inputted string was perfectly balanced as the closed
        #characters matched with the open characters perfectly
        print("balanced")
    else:
        print("not balanced")