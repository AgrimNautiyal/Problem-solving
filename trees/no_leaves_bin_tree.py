#question url : https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1
#to calculate no of leaves in binary tree

#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def helper(leaves, root):
    if root:
        if root.left is None and root.right is None:
            leaves.append(root)
        if root.right:    
            leaves = helper(leaves, root.right)
        if root.left:
            leaves = helper(leaves, root.left)
    
    return leaves
def countLeaves(root):
    # Code here
    return len(helper([], root))
    
