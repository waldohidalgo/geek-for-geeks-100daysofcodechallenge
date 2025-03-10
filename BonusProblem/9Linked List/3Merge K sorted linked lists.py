import heapq
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class Solution:
    def build(self,arr):
        n=len(arr)

        dummy=Node(None)
        curr=dummy
        for i in range(n):
            curr.next=Node(arr[i])
            curr=curr.next
        
        return dummy.next

    def show(self,head):
        curr=head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
        print()
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        dummy=Node(None)
        curr=dummy
        heap=[]
        for head in arr:
                heapq.heappush(heap,(head.data,head))
        while heap:
            _,node=heapq.heappop(heap)
            curr.next=node
            curr=node
            next_node=node.next
            if next_node:
                heapq.heappush(heap,(next_node.data,next_node))
        return dummy.next
    
# arr1=[1,2,3]
# arr2=[4,5]
# arr3=[6,7]
# arr4=[8,9]
arr1=[1,3]
arr2=[8]
arr3=[4,5,6]
sol=Solution()
head1=sol.build(arr1)
head2=sol.build(arr2)
head3=sol.build(arr3)
#head4=sol.build(arr4)
arr=[head1,head2,head3]
sol.show(sol.mergeKLists(arr))
