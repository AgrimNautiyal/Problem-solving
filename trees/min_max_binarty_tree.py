#question url : https://practice.geeksforgeeks.org/problems/max-and-min-element-in-binary-tree/1
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def maxhelper(root, curr):
    if root:
        if root.data > curr:
            curr = root.data
        curr = maxhelper(root.left, curr)
        curr = maxhelper(root.right, curr)
    return curr
def findMax(root):
    return maxhelper(root, root.data)
    
def minhelper(root, curr):
    if root:
        if root.data < curr:
            curr = root.data
        curr = minhelper(root.left, curr)
        curr = minhelper(root.right, curr)
    return curr
def findMin(root):
    return minhelper(root, root.data)