def helper(root, s):
    if root:
        if root.left!=None and root.right == None:
            s.add(root.left.data)
        if root.left==None and root.right!=None:
            s.add(root.right.data)
        s = helper(root.left,s)
        s=helper(root.right,s)
    return s
def noSibling(root):
    # code here
    s=set()
    res= sorted(list(helper(root, s)))
    if len(res)==0:
        return [-1]
    else:
        return res
