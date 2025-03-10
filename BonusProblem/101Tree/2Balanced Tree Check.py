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
    def isBalanced(self, root):
        # code here
        is_balanced=True
        def rec(root):
            nonlocal is_balanced
            if not root or not is_balanced:
                return -1
            hl=1+rec(root.left)

            hr=1+rec(root.right)
            h=max(hl,hr)
            #print("h",h,"hl",hl,"hr",hr)
            if abs(hl-hr)>1:
                is_balanced=False
            return h
        rec(root)
        return is_balanced
    

sol=Solution()
#arr= [10, 20, 30, 40, 60]
#arr=[1, 2, 3, 4, None, None, None, 5]
#arr=[1, 2, None, None, 3]
#arr=[1,2,3,4,5,6,None,8,9,10,11,12,13]
#arr=[1,2,None,3,None,4,None,5,None,6,None]
#arr=[1,2,3,4,None,5,6,7,None,None,None,None,None,8]
#arr=[1,2,3,4,5,6,7,8,None,None,None,None,None,None,None,9]
arr=[10,20,30,40,60]
root=sol.build(arr)
print(sol.isBalanced(root))