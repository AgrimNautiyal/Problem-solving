#question url : https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1

def reverseList(head):
    # Code here
    current = head
    prev= None
    next = None
    
    while(current):
        next = current.next
        current.next=prev
        
        prev= current
        current = next
    return prev

