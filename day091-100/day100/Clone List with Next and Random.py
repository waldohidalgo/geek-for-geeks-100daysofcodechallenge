'''

        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None


class Solution:
    def build(self,arr):
        n=len(arr)
        hs={}
        for i in range(n):
            hs[i+1]=Node(arr[i][0])

        head=hs[1]
        curr=head
        i=1
        while i<=n:
            curr.next=hs.get(i+1,None)
            curr.random=hs.get(arr[i-1][1],None)
            curr=curr.next
            i+=1

        return head

    def show(self,head):
        curr=head
        while curr:
            print("data: ",curr.data,end=" ")
            print("random data",curr.random.data if curr.random else None)
            curr=curr.next
        print()


    def _add_clone_nodes(self,head):
        curr=head
        while curr:
            clone=Node(curr.data)
            clone.next=curr.next
            curr.next=clone
            curr=clone.next

        curr=head
        while curr:
            curr.next.random=curr.random.next if curr.random else None
            curr=curr.next.next
        return head

    def _extract_clone_list(self,head):
        dummy=Node(None)
        curr_dummy=dummy
        curr=head
        while curr:
            curr_dummy.next=curr.next
            curr_dummy=curr_dummy.next
            curr.next=curr.next.next #volver la lista a su estado original
            curr=curr.next

        return dummy.next

    #Function to clone a linked list with next and random pointer.
    def cloneLinkedList(self, head):
        # code here
        head_clone_list=self._add_clone_nodes(head)
        return self._extract_clone_list(head_clone_list)
        
sol=Solution()
arr=[[1, 3], [3, 3], [5, None], [9, 3]]
#arr=[[1, 3], [2, 1], [3, 5], [4, 3], [5, 2]]
#arr=[[7, None], [7, None]]
head=sol.build(arr)
sol.show(head)
head2=sol.cloneLinkedList(head)
sol.show(head2)