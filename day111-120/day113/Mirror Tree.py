from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function

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
    
    def show(self,root):
        res=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            for _ in range(n):
                node=queue.popleft()
                res.append(node.data if node else None)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        while res[-1] is None:
            res=res[:-1]
        return res
            

#Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here

        def chg(root):
            if root is None:
                return
            root.left,root.right=root.right,root.left

            chg(root.left)
            chg(root.right)

        chg(root)
        return root


#arr=[12, 8, 18, 5, 11] 
#arr=[1, 2, 3, 4, None, None, 5, None, None, 6, 7]
#arr=[1, 2, 3, None, None, 4]
arr=[1, 2, 3, 4, 5]
sol=Solution()
root=sol.build(arr)
print(sol.show(root))
print(sol.show(sol.mirror(root)))