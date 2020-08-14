def detectLoop(head):
    #code here
    start = head
    forward = head
    while(start and forward and forward.next):
        start = start.next
        forward = forward.next.next
        if start == forward:
            return True
    return False