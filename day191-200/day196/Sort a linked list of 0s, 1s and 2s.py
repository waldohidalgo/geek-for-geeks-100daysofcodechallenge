
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

	
class Solution:

    def buildList(self,arr,n):
        dummy=Node(None)
        curr=dummy
        for i in range(n):
            curr.next=Node(arr[i])
            curr=curr.next
        return dummy.next
    
    def show(self,head):
        res=""
        while head:
            res+=str(head.data)+" "
            head=head.next
        return res
    def segregate(self, head):
        #code here
        zero_dummy=Node(None)
        one_dummy=Node(None)
        two_dummy=Node(None)

        zero=zero_dummy
        one=one_dummy
        two=two_dummy

        curr=head

        while curr:
            if curr.data==0:
                zero.next=curr
                zero=zero.next
            elif curr.data==1:
                one.next=curr
                one=one.next
            else:
                two.next=curr
                two=two.next
            curr=curr.next

        one.next = two_dummy.next
        zero.next = one_dummy.next if one_dummy.next else two_dummy.next
        two.next = None

        return zero_dummy.next
    

sol=Solution()
arr=[2,0]
n=len(arr)
head=sol.buildList(arr,n)
head2=sol.segregate(head)
print(sol.show(head2))