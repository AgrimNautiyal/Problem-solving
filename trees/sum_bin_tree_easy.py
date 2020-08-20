#question url : https://practice.geeksforgeeks.org/problems/sum-of-binary-tree/1
def helper(root, s):
    if root:
        s+=root.data
        s= helper(root.left, s)
        s = helper(root.right, s)
    return s
def sumBT(root):
    #code
    
    return helper(root, 0)
    