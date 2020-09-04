#program to return longest palindrome length in linked list
#approach used : for each position, compare the right and left(Reversed) lists and get count of commons,
#then compare the count containing the (prev) node and in the samee loop keep reversing left list after every current node traversal, update after
#every max
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
def count_commons(l1, l2):
    t1 = l1
    t2 = l2
    count = 0
    while(t1 and t2):
        if t1.data == t2.data:
            count+=1
        else:
            break
        t1= t1.next
        t2 = t2.next
    return count
    
def maxPalindrome(head):
    # Code here
    if head == None:
        return 0
    if head.next == None:
        return 1
    result = 1
    curr = head
    prev = None
    next = None
    
    while(curr):
        next =  curr.next
        curr.next = prev
        
        result = max(result, 2*count_commons(prev, next) + 1)
        result = max(result, 2*count_commons(curr, next))
        prev = curr
        curr = next
    return result