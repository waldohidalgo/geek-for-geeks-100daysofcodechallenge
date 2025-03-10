from collections import deque
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

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
    def supplyVaccine(self, root):
        # Your code here
        ct=0
        def rec(root):
            nonlocal ct
            if not root:
                return 0
            l=rec(root.left)
            r=rec(root.right)
            if l==1 or r==1:
                ct+=1
                return 2
            if l==2 or r==2:
                return 0
            return 1
        if rec(root)==1:
            ct+=1
        return ct
        
sol=Solution()
#arr=[1, 2, 3, None, None, None, 4, None, 5, None, 6]
arr=[1,None,2,None,3]
root=sol.build(arr)
print(sol.supplyVaccine(root))