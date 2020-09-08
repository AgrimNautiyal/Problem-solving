def findIntersection(head1, head2):
    # code here
    # return head of intersection list
    s =set()
    t1 = head1
    t2 = head2
    
    ints=None
    res=ints
    while(t2):
        s.add(t2.data)
        t2=t2.next
    while(t1):
        if t1.data in s:
            #o(1) lookup
            if ints == None:
                ints = Node(t1.data)
                res=ints
            else:
                ints.next = Node(t1.data)
                ints=ints.next
        t1 = t1.next
    return res