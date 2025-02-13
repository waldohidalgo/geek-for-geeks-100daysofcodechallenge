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
    def diameter(self, root):
        # Your code here
        max_width=0

        def dfs(root):
            nonlocal max_width
            if root is None:
                return 0
            
            ld=1+dfs(root.left) if root.left else 0
            rd=1+dfs(root.right) if root.right else 0
            max_width=max(max_width,ld+rd)
            return max(ld,rd)
        dfs(root)
        return max_width


arr=[5,1,55]
 
sol=Solution()
root=sol.build(arr)
print(sol.diameter(root))