def getNthfromEnd(head,n):
    #code here
    count = 1
    l = []
    #reverse the linkedlist first and then access n'th element
    while(head):
        l.append(head.data)
        head = head.next
    try:
        return l[::-1][n-1]
    except : 
        return -1