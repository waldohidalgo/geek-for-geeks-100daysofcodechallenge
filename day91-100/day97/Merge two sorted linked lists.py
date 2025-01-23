
class Node:
    def __init__(self, data):   # data -> value stored in node
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

    def sortedMerge(self,head1, head2):
        # code here
        curr1,curr2=head1,head2
        head=Node(None)
        curr=head
        while curr1 and curr2:
            if curr1.data<=curr2.data:
                curr.next=curr1
                curr1=curr1.next
            else:
                curr.next=curr2
                curr2=curr2.next
            curr=curr.next

        while curr1:
            curr.next=curr1
            curr1=curr1.next
            curr=curr.next

        while curr2:
            curr.next=curr2
            curr2=curr2.next
            curr=curr.next
        return head.next

sol=Solution()
arr1=[1,1]
arr2=[2,4]
head1=sol.build(arr1)
head2=sol.build(arr2)
head=sol.sortedMerge(head1,head2)
sol.show(head)
