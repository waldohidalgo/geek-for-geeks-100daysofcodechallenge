class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    

    def createLinkedList(self, arr):
        self.head = None
        current=None
        for i in range(len(arr)):
            if self.head == None:
                self.head = Node(arr[i])
                current = self.head
            else:
                current.next = Node(arr[i])
                current = current.next
        return self.head
    

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        i=head
        j=head
        for _ in range(n):
            j=j.next
        while j:
            i=i.next
            j=j.next
        sum_n=0
        while i:
            sum_n+=i.data
            i=i.next
        return sum_n
        
lkls=LinkedList()
arr=[1,2]
n=2
head=lkls.createLinkedList(arr)
print(Solution().sumOfLastN_Nodes(head,n))