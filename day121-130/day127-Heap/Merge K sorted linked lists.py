import heapq
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None

class Solution:
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