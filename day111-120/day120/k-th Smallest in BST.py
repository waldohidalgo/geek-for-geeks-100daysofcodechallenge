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
# Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        ct=0
        curr=root
        while curr:
            if not curr.left:
                ct+=1
                if ct==k:
                    return curr.data
                curr=curr.right
            else:
                inpred=curr.left
                while inpred.right and inpred.right!=curr:
                    inpred=inpred.right

                if inpred.right==curr:
                    inpred.right=None
                    ct+=1
                    if ct==k:
                        return curr.data
                    curr=curr.right
                else:
                    inpred.right=curr
                    curr=curr.left
        return -1
    
sol=Solution()
# arr=[20, 8, 22, 4, 12, None, None, None, None, 10, 14]
# k=3
arr=[2, 1, 3]
k=2
root=sol._build(arr)
print(sol.kthSmallest(root,k))