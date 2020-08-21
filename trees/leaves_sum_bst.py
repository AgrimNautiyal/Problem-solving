#question url : https://practice.geeksforgeeks.org/problems/sum-of-leaf-nodes-in-bst/1
#sumof leaves of bst
##Structure of node
'''
class Node:
    data=0
    left=None
    right=None

'''
def helper(root, s):
    if root:
        if root.left is None and root.right is None:
            s = s+ root.data
        s = helper(root.left, s)
        s = helper(root.right, s)
    return s
##Complete this function
def sumOfLeafNodes(root):
    ##Your code here
    return helper(root, 0)