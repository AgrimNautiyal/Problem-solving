#question url :https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
#approach is to reverse linked list and then count n times and access the most current node

#User function Template for python3
'''
	Your task is to return the data stored in
	the nth end from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def getNthfromEnd(head,n):
    #code here
    count = 1
    
    #reverse the linkedlist first and then access n'th element
    
    current = head
    prev=None
    next=None
    
    while(current):
        next = current.next
        current.next = prev

        prev = current
        current= next
    #now prev is our head pointer
    
    
    while(count<n and prev):
        prev = prev.next
        count+=1
    if prev :return prev.data
    else:return -1