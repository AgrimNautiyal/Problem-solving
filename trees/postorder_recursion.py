#User function Template for python3


'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def helper(root, l):
    if root:
        l = helper(root.left, l)
        l = helper(root.right, l)
        l.append(root.data)
    return l
def postOrder(root):
    '''
    :param root: root of the given tree.
    :return the list containing post order traversal of the given binary tree.
    '''
    # code here
    #lets try with recursion
    return helper(root, [])
