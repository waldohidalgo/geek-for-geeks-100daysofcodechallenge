class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class Solution:
    def _build(self,arr,pos):
        head=Node(None)
        curr=head
        i=1
        aux=None
        while i<=len(arr):
            curr.next=Node(arr[i-1])
            if i==pos:
                aux=curr.next
            curr=curr.next
            i+=1
        curr.next=aux
        return head.next
    def _show(self,n,head):
        curr=head
        i=0
        while i<n:
            print("act",curr.data)
            print("next",curr.next.data if curr.next else None)
            i+=1
            curr=curr.next
    def _exist_node_loop(self,head):
        curr_one_step=head
        curr_two_step=head
        while curr_two_step or curr_one_step!=curr_two_step:
            if curr_two_step.next is None or curr_two_step.next.next is None:
                return None
            if curr_one_step.next==curr_two_step.next.next:
                return  curr_one_step.next
            curr_one_step=curr_one_step.next
            curr_two_step=curr_two_step.next.next
        return None
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        node=self._exist_node_loop(head)
        if node is None:
            return
        curr1=head
        curr2=node
        if curr1==curr2:
            while curr1.next!=head:
                curr1=curr1.next
            curr1.next=None
        else:
            prev2=None
            while curr1!=curr2:
                prev2=curr2
                curr1=curr1.next
                curr2=curr2.next
            prev2.next=None          


sol=Solution()
arr=[1,2,3,4]
pos=1
head=sol._build(arr,pos)
sol._show(len(arr),head)
print("-")
sol.removeLoop(head)
sol._show(len(arr),head)