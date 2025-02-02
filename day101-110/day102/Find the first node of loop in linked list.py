class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
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
    
    def findFirstNode(self, head):
        #code here
        node=self._exist_node_loop(head)
        if node:
            curr1=head
            curr2=node
            while curr1!=curr2:
                curr1=curr1.next
                curr2=curr2.next
            return curr1.data            
        else:
            return -1


sol=Solution()
arr=[1,3,2,4,5]
pos=2
head=sol._build(arr,pos)
sol._show(len(arr),head)
print(sol.findFirstNode(head))
