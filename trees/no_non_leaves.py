#question url : https://practice.geeksforgeeks.org/problems/count-non-leaf-nodes-in-tree/1
def helper(root, count):
    if root:
        if root.left or root.right:
            count+=1
        count = helper(root.left, count)
        count =helper(root.right, count)
    return count

# function should return the count of total number of non leaf nodes in the tree
def countNonLeafNodes(root):
    
    # add code here
    return helper(root,0)