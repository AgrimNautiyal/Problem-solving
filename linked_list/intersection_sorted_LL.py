def findIntersection(head1,head2):
    #return head
    ints=None
    res=ints
    
    t1=head1
    t2 = head2
    
    while(t1 and t2):
        #if t1>t2, advance t2
        if t1.data > t2.data :
            t2 = t2.next
        #if t2>t1 advance t1
        if t2.data > t1.data : 
            t1 = t1.next
        if t1.data == t2.data :
            if ints == None:
                ints = Node(t1.data)
                res=ints
            else:
                ints.next = Node(t1.data)
                ints=ints.next
            t1= t1.next
            t2= t2.next
        
    return res