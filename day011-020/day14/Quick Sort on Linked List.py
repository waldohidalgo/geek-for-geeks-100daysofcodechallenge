class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def buildList(self,arr):
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
    
    def print(self,head):
        current = head
        s = ""
        while current:
            if current.next:
                s += "Node(" + str(current.data) + ") -> "
            else:
                s += "Node(" + str(current.data) + ")"
            current = current.next
        print(s)

def partition(head, pivotValue):
    left_head = left_tail = None
    right_head = right_tail = None
    current = head
    
    while current:
        next_node = current.next  
        current.next = None      

        if current.data < pivotValue:
            if left_head is None:
                left_head = left_tail = current
            else:
                left_tail.next = current
                left_tail = current
        else:
            if right_head is None:
                right_head = right_tail = current
            else:
                right_tail.next = current
                right_tail = current
        current = next_node
    
    return left_head, right_head

def quickSort(head):
    if head is None or head.next is None:
        return head
    
    pivotValue = head.data
    left_head, right_head = partition(head.next, pivotValue)
    
    left_sorted_head, left_sorted_tail = quickSort(left_head), None
    if left_sorted_head:
        left_sorted_tail = left_sorted_head
        while left_sorted_tail.next:
            left_sorted_tail = left_sorted_tail.next
        left_sorted_tail.next = head
    
    head.next = quickSort(right_head)
    
    return left_sorted_head if left_sorted_head else head  


    
lk=LinkedList()
arr=[1,9,3,8,4,7,2]
head=lk.buildList(arr)
#lk.print(head)
new_head=quickSort(head)
lk.print(new_head)
#lk.print(rightPartition(head.next,1))
