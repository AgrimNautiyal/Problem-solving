#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def preorder(root):
    '''
    :param root: root of the given tree.
    :return: a list containing pre order Traversal of the given tree.
    {
        class Node:
        def _init_(self,val):
            self.data = val
            self.left = None
            self.right = None
    }
    '''
    # code here
    #lets try this without recursion
    stack=[]
    stack.append(root)
    res=[]
    while(len(stack)):
        #follow order Root, Left, Right and hence we'll pop, then push right then push left so that pop is always reversed
        n = stack.pop()
        res.append(n.data)
        
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
    
    return res
        
