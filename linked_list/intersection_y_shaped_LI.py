#question url : https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1
#NAIVE SOLUTION USING SETS for O(1) access time 
def intersetPoint(head_a,head_b):
    #code here
    a=set()

    while(head_a):
        a.add(head_a)
        if head_a.next:
            head_a = head_a.next
        else:
            head_a=None
    while(head_b):
        if head_b in a:
            return head_b.data
        if head_b.next:
            head_b = head_b.next
        else:
            head_b=None
    
    return -1