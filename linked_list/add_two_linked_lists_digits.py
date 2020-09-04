#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def addLists(first, second):
    # code here
    # return head of sum list
    #first we will reverse the two linked llists given to us and then perform the addition operation
    
    prev_first = None
    next=None 
    curr=first
    
    while(curr):
        next=  curr.next
        curr.next = prev_first
        
        prev_first = curr
        curr = next
    #prev_first contains our pointer
    
    #let us reverse the next list
    prev_second = None
    next = None
    curr= second
    
    while(curr):
        next = curr.next
        curr.next= prev_second
        
        prev_second = curr
        curr = next
    #prev_second contains our head pointer
    
    hf = prev_first
    hs = prev_second
    

    #both linked lists are reversed so now we can add them and then 
    carry = 0
    temp=Node(-1)
    tmp_cpy=temp
    while(hf!=None or hs!=None):
        
        
        if hf!=None:
            a = hf.data
        else:
            a = 0
        if hs!=None:
            b = hs.data
        else:
            b = 0
        sum = (a+b) + carry
        carry = sum//10
        sum = sum%10
        
        new = Node(sum)
        temp.next = new
        temp = new
        
        if hf!=None: hf = hf.next
        if hs!=None: hs = hs.next
        
    if carry!=0:
        temp.next=Node(carry)
    tmp_cpy = tmp_cpy.next
    #now lets reverse it 
    head = tmp_cpy
    
    prev=None
    next = None
    curr = head
    while(curr):
        next=  curr.next
        curr.next = prev
        
        prev = curr
        curr = next
    return prev
    
        

