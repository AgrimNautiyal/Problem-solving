#User function Template for python3


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
def helper(root, l):
    if root:
        l =helper(root.left, l)
        l.append(root.data)
        l=helper(root.right, l)
    return l
def InOrder(root):
    # code here
    #lets try with recursion
    return helper(root, [])


