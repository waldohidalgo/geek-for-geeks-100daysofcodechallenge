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
    def isSymmetric(self, root):
        # Your Code Here
        def rec(root1,root2):
            if not root1 and not root2:
                return True
            elif not root1 and root2 or root1 and not root2:
                return False
            if root1.data!=root2.data:
                return False
            return rec(root1.left,root2.right) and rec(root1.right,root2.left)
        
        return rec(root.left,root.right)
        
sol=Solution()
arr=[1, 2, 2, None, 3, None, 3]
root=sol.build(arr)
print(sol.isSymmetric(root))