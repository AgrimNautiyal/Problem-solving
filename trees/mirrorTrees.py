#check for mirror trees
def areMirror(root1,root2):
    '''
    :param root1,root2: two root of the given trees.
    :return: True False
    
    '''
    #code here
    if root1 is None and root2 is None:
        return True
    if (root1 is None and root2 is not None) or (root2 is None and root1 is not None):
        return False
    
    return root1.data==root2.data and areMirror(root1.left,root2.right) and areMirror(root1.right, root2.left)
    
