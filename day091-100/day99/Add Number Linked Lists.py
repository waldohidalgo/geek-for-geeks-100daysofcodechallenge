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

    def _remove_lead_zeros(self,head):
        curr=head
        while curr.data==0 and curr.next:
            curr=curr.next
        return curr

    def _invert_list(self,head):
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

    def addTwoLists(self, num1, num2):
        # code here
        head=Node(None)
        curr=head
        num1,num2=self._remove_lead_zeros(num1),self._remove_lead_zeros(num2)
        curr1,curr2=self._invert_list(num1),self._invert_list(num2)
        carry=0
        while curr1 and curr2:
            value=carry+curr1.data+curr2.data
            remainder=value%10
            carry=value//10
            curr.next=Node(remainder)
            curr=curr.next
            curr1,curr2=curr1.next,curr2.next
        
        while curr1:
            value=carry+curr1.data
            remainder=value%10
            carry=value//10
            curr.next=Node(remainder)
            curr=curr.next 
            curr1=curr1.next 

        while curr2:
            value=carry+curr2.data
            remainder=value%10
            carry=value//10
            curr.next=Node(remainder)
            curr=curr.next 
            curr2=curr2.next   

        if carry:
            curr.next=Node(carry)

        return self._invert_list(head.next)                  

sol=Solution()
arr1=[4,5]
arr2=[3,4,5]
head1=sol.build(arr1)
head2=sol.build(arr2)
sol.show(sol.addTwoLists(head1,head2))          