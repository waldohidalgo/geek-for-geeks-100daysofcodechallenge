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
    
    def sumK(self,root,k):
        # code here
        count_path=0
        def rec(root,hs,acum):
            nonlocal count_path
            if root is None:
                return
            acum+=root.data
            if acum-k in hs:
                count_path+=hs[acum-k]
            hs[acum]=hs.get(acum,0)+1
            rec(root.left,hs,acum)
            rec(root.right,hs,acum)
            # backtracking
            hs[acum]-=1
        rec(root,{0:1},0)
        return count_path
    
sol=Solution()
arr=[8,4,5,3,2,None,2,3,-2,None,1]
k=7
# arr=[1,2,3]
# k=3
# arr=[-3,1,2,-4,-3,-5,-3]
# k=-3
root=sol._build(arr)

print(sol.sumK(root,k))
