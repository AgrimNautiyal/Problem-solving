#question url : https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1
#I HAD BEEN AVOIDING THIS QUESTION FOR SO LONG, FINALLY GOT IT DONE AND IT TURNED OUT TO ACTUALLY BE PRETTY EASY

#Your task is to complete this function
#function should return head to the DLL




#my code starts from here : 
def inorder(root, trav):
    if root:
        trav = inorder(root.left, trav)
        trav.append(root)
        trav = inorder(root.right, trav)
    
    return trav
def bToDLL(root):
    # do Code here
    #left, right = prev, next
    inorder_trav = inorder(root, [])
    head=None
    l = len(inorder_trav)
    if l == 1:
        head = root
        head.left = None
        head.right= None
        return head
    for i in range(0, l):
        if i != 0 and i!=l-1:
            inorder_trav[i].left=inorder_trav[i-1]
            try:
                inorder_trav[i].right = inorder_trav[i+1]
            except:
                continue
        else:
            if i == 0:
                
                inorder_trav[i].left=None
                try:
                    inorder_trav[i].right = inorder_trav[i+1]
                except:
                    continue
                head = inorder_trav[i]
            else:
                inorder_trav[i].right=None
                inorder_trav[i].left = inorder_trav[i-1]

    return head