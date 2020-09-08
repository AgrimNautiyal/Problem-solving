def check(root, a, b):
    if root:
        if (root.left == a and root.right == b) or (root.left ==b and root.right==a):
            return False
        return check(root.left, a, b) and check(root.right, a, b)
    return True
def isCousin(root, a, b):
    # Your code here
    if check(root, a, b)==False:
        return False
    q=[]
    q.insert(0, root)
    tmp=set()
    while(len(q)):
        l = len(q)
        for i in range(l):
            n = q.pop()
            tmp.add(n.data)
            if n.left:
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)
        if a in tmp and b in tmp:
            return True
        tmp.clear()
    return False