
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:

    def build(self,arr):

        n=len(arr)
        i=0
        head=None
        curr=None
        while i<n:
            if not head:
                head=Node(arr[i])
                curr=head
            else:
                curr.next=Node(arr[i])
                curr=curr.next
            i+=1
        if curr:
            curr.next=None
        return head


    def show(self,head):
        curr=head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
        print()
        
    def reverseList(self, head):
        # Code here
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next 
        return prev
    
sol=Solution()
arr=[2]
head=sol.build(arr)
sol.show(head)
sol.show(sol.reverseList(head))
                                    
