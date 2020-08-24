#question url : https://practice.geeksforgeeks.org/problems/number-of-root-to-leaf-paths/1
#no of root leaf paths (cached output form)
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
# Your task is to complete this function
# Function should print all possible lengths
# print a new at end of function
def helper(root, cur, final):
    if root:
        cur.append(root.data)
        final = helper(root.left, cur, final)
        final = helper(root.right, cur, final)
        if root.left is None and root.right is None:
            final.append(cur[:])
        cur.pop()

    return final
def pathCounts(root):
    # Code here
    paths = helper(root, [], []) # [[1,2,3], [1,4,5], [1, 8]] ... so on
    #print(paths)
    #we need to print in order of length and frequency
    
    
    cache={}
    
    for i in paths:
        l = len(i)
        if l not in cache:
            cache[l]  = 1
        else:
            cache[l] += 1
            
    for i, j in cache.items():
        print(i, j, "$", end='')
    print('')