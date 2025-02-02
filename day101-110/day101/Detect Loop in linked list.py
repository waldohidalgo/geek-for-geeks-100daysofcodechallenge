class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Return boolean value True or False

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

    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        curr_one_step=head
        curr_two_step=head
        while curr_two_step or curr_one_step!=curr_two_step:
            if curr_two_step.next is None or curr_two_step.next.next is None:
                return False
            if curr_one_step.next==curr_two_step.next.next:
                return True
            curr_one_step=curr_one_step.next
            curr_two_step=curr_two_step.next.next
        return False
            

sol=Solution()
arr=[1,2,3,4,5,6,7,8,9]
pos=3
head=sol._build(arr,pos)
sol._show(len(arr),head)
print(sol.detectLoop(head))