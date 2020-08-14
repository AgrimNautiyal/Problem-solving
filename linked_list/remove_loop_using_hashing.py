#question url : https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1
def removeLoop(head):
    # code here
    # remove the loop without losing any nodes
    tmp = head
    s=set()
    s.add(tmp)
    while(tmp.next):
        if tmp.next not in s:
            s.add(tmp.next)
            tmp = tmp.next
        else:
            break
    
    if tmp.next:
        tmp.next=None