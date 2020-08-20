#question url : https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# return a list containing the zig zag level order traversal of the given tree
def zigZagTraversal(root):
    # Your code here
    #we will follow the level order traversal method here
    
    l = []
    q=[]
    q.insert(0, root)
    counter=1
    while(len(q)):
        tmp = []
        ls = len(q)
        for i in range(ls):
            n = q.pop()
            tmp.append(n.data)
            if n.left:
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)
                
        if counter == 1:
            counter*=-1
            l.append(tmp)
        else:
            counter*=-1
            l.append(tmp[::-1])
    l = [j for sub in l for j in sub] 
    return l

