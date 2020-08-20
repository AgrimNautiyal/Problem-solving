#question url : https://practice.geeksforgeeks.org/problems/sum-of-leaf-nodes-at-min-level/1
'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

def minLeafSum(root):
    #return: the sum of all the leaf nodes that are at the minimum level of the binary tree.
    
    #code here
    q=[]
    q.insert(0, root)
    while(len(q)):
        tmp=[]
        lvl_size = len(q)
        for i in range(lvl_size):
            try:
                n = q.pop()
                
                if n.left is None and n.right is None:
                    tmp.append(n.data)
                if n.left:
                    q.insert(0, n.left)
                if n.right:
                    q.insert(0, n.right)
            except:
                continue
        if len(tmp):
            break
    return sum(tmp)
