class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
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
    def printList(self,head):
        current=head
        while current:
            print(f"Node({current.data})",end=" ")
            current=current.next
        print()

class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
        current=head
        new_node=Node(x)
        while current.next and current.next.data<=x:
            current=current.next
        if current==head and current.data>=x:
            new_node.next=head
            head.prev=new_node
            return new_node
        new_node.next=current.next
        if current.next:
            current.next.prev=new_node
        current.next=new_node
        new_node.prev=current
        return head
           
        
    

# arr=[3,5,8,10,12]
arr=[1001,2442,6971,9402]
ll=LinkedList()
for i in arr:
    ll.push(i)

#ll.printList(ll.head)
sol=Solution()
head=sol.sortedInsert(ll.head,6971)
ll.printList(head)