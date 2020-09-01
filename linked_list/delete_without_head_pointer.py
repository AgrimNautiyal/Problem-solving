#User function Template for python3
'''
    Your task is to delete the given node from
	the linked list, without using head pointer.
	
	Function Arguments: node (given node to be deleted) 
	Return Type: None, just delete the given node from the linked list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
def deleteNode(curr_node):
    #code here
    if curr_node.next != None:
        #this means that there is a next node
        curr_node.data = curr_node.next.data
        if curr_node.next.next:
            curr_node.next = curr_node.next.next
        else:
            curr_node.next = None
    else:
        #this means we are at last node
        curr_node= None
