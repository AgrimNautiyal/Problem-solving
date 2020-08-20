#question url: https://practice.geeksforgeeks.org/problems/level-of-a-node-in-binary-tree/1
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def getLevel(root,target):
    '''
    :param root: root of given tree.
    :param target: target to find level
    :return: LEVEL NO
    '''
    # code here
    #we will follow principle of level order traversal
    q = []
    q.insert(0, root)
    lvl=1
    while(len(q)):
        lvl_size = len(q)
        for i in range(lvl_size):
            n = q.pop()
            if n.data == target:
                return lvl
            if n.left : 
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)
        lvl+=1
    return 0