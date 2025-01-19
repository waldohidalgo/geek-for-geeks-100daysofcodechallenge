class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        current=self.head
        while current.next:
            current=current.next
        current.next = Node(new_data)
    def printList(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next


class Solution:
    def count(self, head, key):
        # Code here
        count=0
        current=head
        while current:
            if current.data==key:
                count+=1
            current=current.next
        return count
    
#arr=[1,2,1,2,1,3,1]
arr=[1,2,1,2,1]
lkls=LinkedList()
for i in arr:
    lkls.push(i)
#lkls.printList()
sol=Solution()
print(sol.count(lkls.head,3))