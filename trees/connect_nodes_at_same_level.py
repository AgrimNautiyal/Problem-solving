#question : to connect nodes at same level of tree
#question URL : https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1
def connect(root):
    '''
    :param root: root of the given tree
    :return: none, just connect accordingly.
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
                self.nextRight = None
    }
    '''
    #idea is to perform level order traversal and connect each node within
    #the list
    
    #final = []
    q=[]
    q.insert(0, root)
    
    while(len(q)):
        prev=None
        #tmp= []
        lvl_size = len(q)
        for i in range(lvl_size):
            n = q.pop()
            if prev==None:
                prev=n
            else:
                prev.nextRight=n
                prev=n
            #tmp.append(n)
            if n.left:
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)
        prev.rightNext=None
        #final.append(tmp)