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
            if i<n and arr[i]!=None:
                left=Node(arr[i])
                curr_root.left=left
                queue.append(left)
            i+=1
            if i<n and arr[i]!=None:            
                right=Node(arr[i])
                curr_root.right=right
                queue.append(right)

        return root
    def distributeCandy(self, root):
        # your code here
        moves=0
        def rec(root):
            nonlocal moves
            if not root:
                return 0
            left=rec(root.left)
            right=rec(root.right)

            balance=root.data-1+left+right

            moves+=abs(balance)
            return balance
        rec(root)
        return moves


sol=Solution()
arr=[0,3,2,0,0,0,0]
root=sol.build(arr)
print(sol.distributeCandy(root))