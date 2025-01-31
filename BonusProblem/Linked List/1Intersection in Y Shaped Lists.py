
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def _get_len(self,head):
        curr=head
        ct=0
        while curr:
            ct+=1
            curr=curr.next
        return ct

    def intersectPoint(self, head1, head2):
        # code here
        len1=self._get_len(head1)
        len2=self._get_len(head2)
        curr1,curr2=head1,head2
        while len1>len2:
            len1-=1
            curr1=curr1.next
        while len1<len2:
            len2-=1
            curr2=curr2.next
        while curr1 and curr2 and curr1!=curr2:
            curr1=curr1.next
            curr2=curr2.next
        return curr1
    
arr1=[3,2,7,9,10,7]
arr2=[3,3,5,9,10,7]
sol=Solution()
head1=sol.build(arr1)
head2=sol.build(arr2)
print(sol.intersectPoint(head1,head2))