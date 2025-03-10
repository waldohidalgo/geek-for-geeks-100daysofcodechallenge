from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def build(self,arr):
        n=len(arr)
        root=Node(arr[0])
        queue=deque([root])
        i=0
        while i<n:
            curr_root=queue.popleft()
            i+=1
            if i<n and arr[i]:
                left=Node(arr[i])
                curr_root.left=left
                queue.append(left)
            i+=1
            if i<n and arr[i]:            
                right=Node(arr[i])
                curr_root.right=right
                queue.append(right)

        return root
    def getCount(self, root, l, h):
        # Your code here
        count=0
        def rec(root,l,h):
            nonlocal count
            if not root:
                return
            if l<=root.data<=h:
                count+=1
                rec(root.left,l,h)
                rec(root.right,l,h)
            elif root.data>h:
                rec(root.left,l,h)
            elif root.data<l:
                rec(root.right,l,h)
        rec(root,l,h)
        return count

sol=Solution()
arr= [1, 2, 3]
l = 23
h = 95
root=sol.build(arr)
print(sol.getCount(root,l,h))