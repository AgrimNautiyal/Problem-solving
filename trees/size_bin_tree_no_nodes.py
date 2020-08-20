#question url : https://practice.geeksforgeeks.org/problems/size-of-binary-tree/1
# Your task to complete this function
# function should return size of the binary tree as integer

def helper(root, size):
    if root:
        size+=1
        size = helper(root.left, size)
        size = helper(root.right, size)
    return size
def getSize(node):
    # code here
    return helper(node, 0)

