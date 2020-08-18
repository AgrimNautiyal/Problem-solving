#question url : https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1
# Class to represent a node
class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:

    # The method push to push element into
    # the stack
    def __init__(self):
        self.head = None
        
    def push(self, data):

        # Add code here

        # The method pop which return the element
        # poped out of the stack
        if self.head is None:
            self.head=  StackNode(data)
        else:
            tmp = self.head
            
            while(tmp.next):
                tmp = tmp.next
            tmp.next = StackNode(data)

    def pop(self):
        
        
        if self.head is None:
            return -1
        if self.head.next is None:
            data = self.head.data
            self.head =None
            return data
        tmp = self.head
        # Add code here
        while(tmp.next.next):
            tmp=tmp.next
        data = tmp.next.data
        tmp.next = None
        return data

    def view(self):
        l = []
        tmp = self.head
        while(tmp):
            l.append(tmp.data)
            tmp = tmp.next
        return l