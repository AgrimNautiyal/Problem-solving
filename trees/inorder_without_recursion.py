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
def InOrder(root):
    # code here
    #lets try without recursion using a stack
    
    stack=[]
    res=[]
    while(True):
        while(root!=None):
            stack.append(root)
            root = root.left
            
        if len(stack)==0:
            break
        root = stack.pop()
        res.append(root.data)
        root = root.right
    return res