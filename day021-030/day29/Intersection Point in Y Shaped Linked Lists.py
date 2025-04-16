class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def getLength(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def intersetPoint(head1,head2):
    #code here
    len1=getLength(head1)
    len2=getLength(head2)
    diff=len1-len2
    if diff>0:
        for i in range(diff):
            head1=head1.next
    else:
        for i in range(abs(diff)):
            head2=head2.next
    while head1 and head2:
        if head1==head2:
            return head1.data
        head1=head1.next
        head2=head2.next
    return -1


def intersectPoint(head1, head2):
    h1 = head1
    h2 = head2
    while h1 != h2:
        h1 = h1.next if h1 else head2
        h2 = h2.next if h2 else head1
    return h1.data if h1 else -1
