#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
def findMid(head):
    # Code here
    # return the value stored in the middle node
    mid = head
    last = head
    while(last):
        if last.next == None:
            return mid
        if last.next.next== None:
            return mid
        mid = mid.next
        last = last.next.next
    return mid

def merge(a1, a2):
    tmp=Node('start')
    tmp_cpy = tmp
    t1 = a1
    t2 = a2
    while(t1 and t2):
        if t1.data >= t2.data:
            tmp.next= t2
            t2 = t2.next
        else:
            tmp.next = t1
            t1 = t1.next
        tmp = tmp.next
    while(t1):
        tmp.next = t1
        t1 = t1.next
        tmp = tmp.next
    while(t2):
        tmp.next=  t2
        t2 = t2.next
        tmp = tmp.next
    return tmp_cpy.next
        
    
    
def sortDoubly(head):
    #Your code here
    if head.next == None or head == None:
        return head
    mid = findMid(head)
    end = mid.next
    mid.next=  None
    start = sortDoubly(head)
    end = sortDoubly(end)
    return merge(start, end)


