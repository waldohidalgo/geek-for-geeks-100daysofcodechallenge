from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def _build(self,arr):
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
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def rec(root,low,high):
            if not root:
                return True
            if not low<root.data<high:
                return False
            return rec(root.right,root.data,high) and rec(root.left,low,root.data)
        return rec(root,float("-inf"),float("inf"))
    
sol=Solution()
arr=[2, 1, 3, None, None, None, 5]
root=sol._build(arr)
print(sol.isBST(root))