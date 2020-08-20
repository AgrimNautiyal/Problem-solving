#question url : https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reversePrint(root):
    '''
    :param root: root of given tree.
    :return: print reverse level order traversal , no need to print next line.
    '''
    # code here
    l = []
    q=[]
    q.insert(0, root)
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
                
        l.append(tmp)
    l=l[::-1]
    l = [j for sub in l for j in sub]
    print(' '.join(map(str, l)))
