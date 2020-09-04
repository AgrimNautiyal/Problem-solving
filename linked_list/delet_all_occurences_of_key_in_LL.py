#delete occurences of element k in a linked list
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteAllOccurances(head, k):
    # Code here
    tmp = head
    while(True):
        if head.data == k:
            head= head.next
        else:
            break
    #now in the beginning all the initial kets are deleted
    while(tmp.next):
        if tmp.next.data == k:
            tmp.next = tmp.next.next
        else:
            tmp = tmp.next
    return head

