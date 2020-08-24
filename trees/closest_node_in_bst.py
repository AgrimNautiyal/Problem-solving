#question url : https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1
def helper(root, K, m):
    if root:
        m.append(abs(root.data - K))
        m= helper(root.left, K, m)
        m= helper(root.right, K, m)
    return m
def minDiff(root, K):
    # code here
    m = []
    return min(helper(root, K, m))
