#User function Template for python3
'''
IDEA IS TO MIMIC PREORDER BUT SWAP THE L,R AND THEN REVERSE FINAL LIST
Because : Pre-order : Rt, L, R and Post-order : L, R, Rt, so if we can do a pre-order with Rt, R, L and then swap R,L then reverse, we get post.
'''

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def postOrder(root):
    
    # code here
    #lets try without recursion but using 2 stacks
    stack1 = []
    stack2 = []
    
    stack1.append(root)
    
    while(len(stack1)):
        n = stack1.pop()
        stack2.append(n.data)
        
        if n.left:
            stack1.append(n.left)
        if n.right:
            stack1.append(n.right)
            
    return stack2[::-1]
        







