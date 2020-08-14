#question url : https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
#less naive solution : works with hashing since set access is o(1)
def detectLoop(head):
    #code here
    s =set()
    while(head):
        if head in s:
            return True
        else:
            s.add(head)
            if head.next: head= head.next
            else: head=None
    return False
        