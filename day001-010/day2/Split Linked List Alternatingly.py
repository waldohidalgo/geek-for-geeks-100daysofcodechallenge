#User function Template for python3

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None



class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        first=head
        second=head.next
        temp=head.next.next
        first_pointer=first
        second_pointer=second
        count=2
        while temp:
            if count%2==0:
                first_pointer.next=temp
                first_pointer=first_pointer.next
            else:
                second_pointer.next=temp
                second_pointer=second_pointer.next
            temp=temp.next
            count+=1
        first_pointer.next=None
        second_pointer.next=None
        return [first,second]