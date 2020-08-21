#question url : https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
#reverse first k elements of queue
'''
Function Arguments :
		@param  : queue ( given queue to be used), k(Integer ),n(size of queue)
		@return : lsit, just reverse the first k elements of queue and return new queue
'''

def reverseK(queue,k,n):
    # code here
    q1 = []
    stack = []
    for i in range(n-k):
        q1.insert(0, queue.pop())
    for i in range(k):
        stack.append(queue.pop())
    while(len(stack)):
        q1.insert(0, stack.pop())
    
    return q1