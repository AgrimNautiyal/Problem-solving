#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def helper(root, l):
    if root:
        l.append(root.data)
        l = helper(root.left, l)
        l=helper(root.right, l)
    return l
def preorder(root):
    
    #lets try this with recursion
    return helper(root,[])
