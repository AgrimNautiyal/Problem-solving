#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def isPalindrome(head):
    #code here
    #first find mid element then split list into two lists then reverse second list
    #then compare both lists till both of them are not null and return false only in case of mismatch else return true at end of function
    
    start = head
    mid = head
    fast = head
    adjustment = 0
    while(fast):
        
        if fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                #this means mid is exactly at the mid element so we don't need an adjustment
                break
        else:
            adjustment = 1
            #in this case we have an extra element so we need to be careful
            break
        mid = mid.next
    #mid is at start 
    second = mid.next
    mid.next = None
    #now reverse second
    prev=None
    next = None
    curr = second
    while(curr):
        next = curr.next
        curr.next = prev
        
        prev = curr
        curr = next
    second = prev
    #now to compare start and second
    while(start and second):
        if start.data !=second.data:
            return False
        start = start.next
        second = second.next
    return True




