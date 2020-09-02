#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
'''

def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    OH = head
    NH = Node(head.data)
    NT = NH
    S = {}
    
    while(OH):
        #map the next relationship
        if OH.next != None:
            if OH.next in S:
                NT.next = S[OH.next]
            else:
                NN = Node(OH.next.data)
                NT.next = NN
                S[NN] = NN
        
        #map the arb relationship
        if OH.arb != None:
            if OH.arb in S:
                NT.arb = S[OH.arb]
            else:
                NA = Node(OH.arb.data)
                NT.arb = NA
                S[NA] = NA

        if OH.next:
            OH = OH.next
        else:
            break
        if NT.next :
            NT = NT.next
    return NH
        
