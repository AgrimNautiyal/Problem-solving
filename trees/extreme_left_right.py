#to print extreme left and right nodes of each level
'''
class Node:
    def _init_(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

def printCorner(root):
    
    # print corner data, no need to print new line
    # code here
    #level order traversal then print elements
    
    l = []
    q=[]
    
    q.insert(0, root)
    
    while(len(q)):
        lvl = len(q)
        tmp=[]
        for i in range(lvl):
            n =q.pop()
            tmp.append(n.data)
            if n.left:
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)
        if len(tmp) == 1:
            l.append(tmp[0])
        else:
            if len(tmp) > 1:
                l.append(tmp[0])
                l.append(tmp[-1])
    print(' '.join(map(str, l)), end='')

