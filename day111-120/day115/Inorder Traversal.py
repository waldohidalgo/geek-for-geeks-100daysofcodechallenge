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
    # espacio h
    def inOrder(self,root):
        # code here
        res=[]
        def rec(root):
            if root is None:
                return
            rec(root.left)
            res.append(root.data)
            rec(root.right)
        return res
    
    # espacio 1

    def inOrderMorris(self,root):
        res=[]
        curr=root
        while curr:
            if not curr.left:
                res.append(curr.data)
                curr=curr.right
            else:
                inpred=curr.left
                while inpred.right and inpred.right!=curr:
                    inpred=inpred.right

                if inpred.right==curr:
                    inpred.right=None
                    res.append(curr.data)
                    curr=curr.right
                else:
                    inpred.right=curr
                    curr=curr.left
        return res

sol=Solution()
arr=[20, 8, 22, 4, 12, None, None, None, None, 10, 14]
root=sol._build(arr)
print(sol.inOrderMorris(root))