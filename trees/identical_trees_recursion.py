#question url : https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return true/false or 1/0

def isIdentical(root1, root2):
    # Code here
    if root1 is None and root2 is None:
        return True
    if root1 is None and root2:
        return False
    if root1 and root2 is None:
        return False
    
    return root1.data == root2.data and isIdentical(root1.right, root2.right) and isIdentical(root1.left, root2.left)
