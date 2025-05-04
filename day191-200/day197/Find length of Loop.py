
# Node Class
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
    def detectLoop(self, head):
        #code here
        curr_one_step=head
        curr_two_step=head
        while curr_two_step or curr_one_step!=curr_two_step:
            if curr_two_step.next is None or curr_two_step.next.next is None:
                return [False,None]
            if curr_one_step.next==curr_two_step.next.next:
                return [True,curr_one_step.next]
            curr_one_step=curr_one_step.next
            curr_two_step=curr_two_step.next.next
        return [False,None]
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here
        existLoop,node=self.detectLoop(head)
        if existLoop:
            curr=node.next
            count=1
            while curr!=node:
                count+=1
                curr=curr.next 
            return count      
        else:
            return 0
        

sol=Solution()
# arr=[1,2,3,4,5]
# pos=2
# arr=[25,14,19,33,10,21,39,90,58,45]
# pos=4
arr=[0,1,2,3]
pos=None
head=sol._build(arr,pos)
print(sol.countNodesInLoop(head))