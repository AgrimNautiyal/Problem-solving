#reverse string using stack
#question url : https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1
def reverse(string):
    
    #Add code here
    stack = []
    res= []
    
    for i in string:
        stack.append(i)
        
    while(len(stack)):
        res.append(stack.pop())

    return ''.join(res)