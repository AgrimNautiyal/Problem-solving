#question url : https://practice.geeksforgeeks.org/problems/binary-tree-to-cdll/1
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''
def inorder(root, l):
    if root:
        l = inorder(root.left, l)
        l.append(root)
        l = inorder(root.right, l)
    return l
def bTreeToClist(root):
    #Your code here
    l = inorder(root, [])
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        l[0].right = l[1]
        l[0].left = l[1]
        
        l[1].right = l[1].left = l[0]
        
        return l[0]
    #here l is our list containing inorder traversal of binary tree
    #left, right = prev, next
    head = l[0]
    tail = l[-1]
    
    for i in range(1, len(l)-1):
        l[i].left = l[i-1]
        l[i].right = l[i+1]
        
    head.right = l[1]
    head.left = tail
    
    tail.left = l[i]
    tail.right = head
    
    return head