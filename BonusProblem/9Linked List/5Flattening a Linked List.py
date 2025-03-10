
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        


class Solution:
    def _show(self,head):
        curr=head
        while curr:
            print(curr.data,end=" ")
            curr=curr.bottom
        print()

    def _build_bottom(self,arr):
        dummy=Node(None)
        curr=dummy
        for i in range(len(arr)):
            curr.bottom=Node(arr[i])
            curr=curr.bottom
        return dummy.bottom
    
    def _build_next(self,arr):
        dummy=Node(None)
        curr=dummy
        for i in range(len(arr)):
            curr.next=arr[i]
            curr=curr.next
        return dummy.next

    def _join_two_list(self,head1:Node,head2:Node):
        dummy=Node(None)
        curr=dummy
        curr1,curr2=head1,head2
        while curr1 and curr2:
            if curr1.data<curr2.data:
                curr.bottom=curr1
                curr1=curr1.bottom
            else:
                curr.bottom=curr2
                curr2=curr2.bottom
            curr=curr.bottom

        while curr1:
            curr.bottom=curr1
            curr=curr.bottom
            curr1=curr1.bottom

        while curr2:
            curr.bottom=curr2
            curr=curr.bottom
            curr2=curr2.bottom    
        
        return dummy.bottom    

    def flatten(self, root):
        #Your code here
        dummy1=Node(None)
        dummy1.next=root
        curr=dummy1

        dummy2=Node(float('-inf'))
        head=dummy2
        while curr.next:
            head=self._join_two_list(head,curr.next)
            curr=curr.next

        return head.bottom
        
sol=Solution()  

# arr1=[5,7,8,30]
# arr2=[10,20]
# arr3=[19,22,50]
# arr4=[28,35,40,45]

# head1=sol._build_bottom(arr1)
# head2=sol._build_bottom(arr2)
# head3=sol._build_bottom(arr3)
# head4=sol._build_bottom(arr4)
# arr=[head1,head2,head3,head4]
# head=sol._build_next(arr)
# sol._show(sol.flatten(head))

arr1=[5,7,8,30]
arr2=[10]
arr3=[19,22,50]
arr4=[28]
head1=sol._build_bottom(arr1)
head2=sol._build_bottom(arr2)
head3=sol._build_bottom(arr3)
head4=sol._build_bottom(arr4)
arr=[head1,head2,head3,head4]
head=sol._build_next(arr)
sol._show(sol.flatten(head))