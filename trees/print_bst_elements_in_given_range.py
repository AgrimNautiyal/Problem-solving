#question url : https://practice.geeksforgeeks.org/problems/print-bst-elements-in-given-range/1
'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# returns a list of node values in the BST (rooted at 'root')
# that lie in the given range [low, high]
def helper(root, low, high, res):
    if root:
        if root.data >= low and root.data <=high:
            res.append(root.data)
        if root.data > low : 
            res = helper(root.left, low, high, res)
        if root.data < high:
            res = helper(root.right, low, high, res)
    return res
def printNearNodes(root, low, high):
    #code here.
    return sorted(helper(root, low, high, []))

