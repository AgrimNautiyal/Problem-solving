#question url : https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1

##Structure of the node
'''
class Node:
    data=0
    left=None
    right=None

'''
def minValue(root):
    ##Your code here
    if root is None:
        return -1
    if root.left:
        return minValue(root.left)
        
    return root.data
