#question url : https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/1
def getCount(head_node):
    #code here
    count = 0
    while(head_node):
        count+=1
        head_node = head_node.next
    return count