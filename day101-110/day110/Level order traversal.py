from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
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
    
    def show(self,root):
        pass

    def levelOrder(self, root:Node):
        # Your code here
        res=[]
        queue=deque([root])
        while queue:
            arr=[]
            n=len(queue)
            for _ in range(n):
                node=queue.popleft()
                arr.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(arr)

        return res
        
#arr=[1, 3, 2, None, None, None, 4, 6, 5]
#arr=[10, 20, 30, 40, 50]
arr=[1, 2, 3]
sol=Solution()
root=sol.build(arr)
print(sol.levelOrder(root))