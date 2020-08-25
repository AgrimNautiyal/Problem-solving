#https://practice.geeksforgeeks.org/problems/check-for-bst/1

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def inorder(root, l):
    if root:
        l = inorder(root.left, l)
        l.append(root.data)
        l = inorder(root.right, l)
    return l
# return True if the given tree is a BST, else return False
def isBST(root):
    #code here
    t = inorder(root, [])
    
    #if t is sorted then YES else NO
    
    prev = 0
    for i in range(1, len(t)):
        
        if t[i] <= t[prev]:
            return False
        prev+=1
    return True
