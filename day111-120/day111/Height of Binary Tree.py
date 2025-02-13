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
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        max_length=0

        def dfs(root,ct):
            nonlocal max_length
            if root is None:
                max_length=max(max_length,ct)
                return
            ct+=1

            dfs(root.left,ct)
            dfs(root.right,ct)
        dfs(root,-1)
        return max_length
    

#arr=[12, 8, 18, 5, 11] 
arr=[1, 2, 3, 4, None, None, 5, None, None, 6, 7]  

sol=Solution()
root=sol.build(arr)
print(sol.height(root))