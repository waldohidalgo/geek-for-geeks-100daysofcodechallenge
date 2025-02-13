from collections import deque
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

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
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        max_sum=float('-inf')
        def rec(root):
            nonlocal max_sum
            if root is None:
                return 0
            l=rec(root.left)
            r=rec(root.right)
            curr=root.data
            max_single_path=max(curr,curr+l,curr+r)
            root_path=l+curr+r
            max_sum=max(max_sum,max_single_path,root_path)
            return max_single_path
        rec(root)
        return max_sum
    
sol=Solution()
#arr=[10, 2, 10, 20, 1, None, -25, None, None, None, None, 3, 4]
arr= [-17, 11, 4, 20, -2, 10]
root=sol._build(arr)
print(sol.findMaxSum(root))
