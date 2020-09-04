#reverse linked list in k-sized groups

"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def reverse(head, k):
    # Code here
    prev=None
    next=None
    count=0
    current = head
    while(current and count<k):
        next= current.next
        current.next = prev
        
        prev = current
        current = next
        count+=1
    
    if next:
        head.next = reverse(next, k)
    return prev

