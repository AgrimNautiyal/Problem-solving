#https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1
'''
class Node:
    def init(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the level order traversal of the binary tree in spiral order
# Note: You aren't required to print a new line after every test case
def printSpiral(root):
    # Code here
    #first perform level order trav then alternate reverrse for non root levels
    final=[]
    q=[]
    q.insert(0, root)
    
    while(len(q)):
        tmp = []
        lvl_size = len(q)
        for i in range(lvl_size):
            n= q.pop()
            if n:
                tmp.append(n.data)
                if n.left:
                    q.insert(0, n.left)
                if n.right:
                    q.insert(0, n.right)
        final.append(tmp)
    #we have our lvl order traversed list of lists
    
    flag = 1
    #print(final)
    s = ''
    for i in final:
        if len(i) == 1:
            s+=str(i[0]) + " "
            
            continue
        if flag == 1:
            for j in i:
                s+= str(j) + " "
            flag*=-1
        else:
            x= i[::-1]
            for j in x:
                s+= str(j) + " "
            flag*=-1
    print(s)
    #print(final)
    return s