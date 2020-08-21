#question url : https://practice.geeksforgeeks.org/problems/queue-reversal/1/
def reverseQueue(q):
    #add code here
    stack = []
    l = q.qsize()
    
    for i in range(l):
        stack.append(q.get())
    for i in range(l):
        q.put(stack.pop())
        
    return q
