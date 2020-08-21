#question url : https://practice.geeksforgeeks.org/problems/search-a-node-in-bst/1
#search in bst
'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
def helper(node, data):
    if node:
        if node.data == data:
            return True
        if data < node.data : 
            return helper(node.left, data)
        else:
            return helper(node.right, data)
    return False

class BST:
    def search(self, node, data):
        #code here
        return helper(node,data)