
class Node:
    def __init__(self, data):
        self.data = data
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
    
    def reverseKGroup(self, head, k):
        # Code here
        dummy=Node(None)
        dummy.next=head
        prevK=None
        last=dummy
        curr=head
        i=0
        while curr:
            if i%k==0:
                j=0
                curr1=curr
                while j<k and curr1:
                    curr1=curr1.next
                    j+=1
                prevK=curr1
            nextCurr=curr.next
            curr.next=prevK
            prevK=curr
            if i%k==(k-1) or nextCurr is None:
                nextLast=last.next
                last.next=curr
                last=nextLast
            curr=nextCurr
            i+=1
        return dummy.next


arr=[1,2,3,4,5,6,7,8]
k=4
sol=Solution()
head=sol.build(arr)
sol.show(head)
sol.show(sol.reverseKGroup(head,k))       
            

