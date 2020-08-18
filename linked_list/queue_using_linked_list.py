#question url : https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1
# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    
    def __init__(self):
        self.head=None
    # Method to add an item to the queue
    def push(self, item): 
         
         #Add code here
         #first add as a normal list, and then reverse the said linked list
        if self.head is None:
            self.head = Node(item)
        else:
            tmp = Node(item)
            tmp.next = self.head
            self.head = tmp
        
    # Method to remove an item from queue
    def pop(self):
         
         #add code here
        #simple remove last element, traverse through head
        if self.head == None:
            return -1
        if self.head.next is None:
            data = self.head.data
            self.head=None
            return data
            
        tmp = self.head
        while(tmp.next.next):
            tmp = tmp.next
        
        data = tmp.next.data
        tmp.next =None
        return data
            