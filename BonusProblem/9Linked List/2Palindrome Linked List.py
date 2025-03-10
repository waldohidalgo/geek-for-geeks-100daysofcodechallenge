class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
#Function to check whether the list is palindrome.

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


    def isPalindrome(self, head):
        #code here
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev=None
        while slow:
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        curr=head
        while prev:
             if prev.data!=curr.data:
                  return False
             curr=curr.next
             prev=prev.next
        return True

             
                   
    

arr=[1,1]
sol=Solution()
head=sol.build(arr)

print(sol.isPalindrome(head))