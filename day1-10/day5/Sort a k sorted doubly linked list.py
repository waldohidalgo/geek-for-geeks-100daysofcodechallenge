import heapq

class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None


class DLL:
    def createDLL(self, arr):
        head = None
        current = None
        for i in arr:
            if head is None:
                head = DLLNode(i)
                current = head
            else:
                current.next = DLLNode(i)
                current.next.prev = current
                current = current.next
        return head
    def __repr__(self):
        current = self.head
        s = ""
        while current:
            if current.next:
                s += "Node(" + str(current.data) + ") -> "
            else:
                s += "Node(" + str(current.data) + ")"
            current = current.next
        return s
class Solution:


    def sortAKSortedDLL(self, head, k):
        # Code Here
        heap=[]
        current=head
        new_head=None
        current_new_head=None
        current_k=None
        while current:

            if current==head:
                current_k=current
                i=0
                while i<=k and current_k:
                    heapq.heappush(heap,current_k.data)
                    current_k=current_k.next
                    i+=1
                new_head=DLLNode(heapq.heappop(heap))
                current_new_head=new_head
            else:
                if current_k:
                    heapq.heappush(heap,current_k.data)
                    current_k=current_k.next
                new_node=DLLNode(heapq.heappop(heap))
                current_new_head.next=new_node
                new_node.prev=current_new_head
                current_new_head=current_new_head.next
            current=current.next
        return new_head
    
    def display(self,head):
        current = head
        s = ""
        while current:
            if current.next:
                s += "Node(" + str(current.data) + ") -> "
            else:
                s += "Node(" + str(current.data) + ")"
            current = current.next
        return s

        
            
        
            
ddl=DLL()
ddl.head=ddl.createDLL([5,6,7,3,4,4])
#print(ddl)

s=Solution()

print(s.display(s.sortAKSortedDLL(ddl.head,3)))
