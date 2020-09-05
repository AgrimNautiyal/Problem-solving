def mirror(root):
    # Code here
    #lets try without recursion
    q=[]
    q.append(root)
    while(len(q)):
        n = q.pop()
        n.left,  n.right =n.right, n.left
        
        if n.left:
            q.insert(0, n.left)
        if n.right:
            q.insert(0, n.right)