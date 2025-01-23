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

    def size_and_mutate(self,head):
        n=0
        last=head
        while last:
            n+=1
            if last.next:
                last=last.next
            else:
                last.next=head
                break
        return n,last
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        n,end=self.size_and_mutate(head)
        c=k%n
        start=head
        i=0
        while i<=c:
            if i!=c:
                start,end=start.next,end.next
            i+=1
        end.next=None
        head=start 
        return head
            

        

sol=Solution()
arr=[10,11,12]
k=1
head=sol.build(arr)
sol.show(head)
sol.show(sol.rotate(head,k))