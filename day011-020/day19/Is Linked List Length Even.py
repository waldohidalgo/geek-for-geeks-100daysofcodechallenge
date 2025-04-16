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
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(new_data)


class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        return count%2==0
    
ll=LinkedList()
arr=[1]
for i in arr:
    ll.push(i)
print(Solution().isLengthEven(ll.head))