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
    def verticalOrder(self, root): 
        #Your code here
        minm,maxm=float("inf"),float("-inf")
        def ranges(root,s):
            nonlocal minm,maxm
            if not root:
                return
            if s<minm:
                minm=s
            if s>maxm:
                maxm=s
            ranges(root.left,s-1)
            ranges(root.right,s+1)
        ranges(root,0)
        i=-minm if minm<0 else minm
        j=maxm


        arr=[[] for _ in range(i+j+1)]

        def rec(root,s):
            if not root:
                return
            arr[s+i].append(root.data)

            rec(root.left,s-1)
            rec(root.right,s+1)
            
        rec(root,0)
        return arr


    def verticalOrder2(self,root):
        hs={}
        minm,maxm=float("inf"),float("-inf")

        def rec(root,s):
            nonlocal minm,maxm
            if not root:
                return
            if s not in hs:
                hs[s]=[]
            hs[s].append(root.data)
            
            if s>maxm:
                maxm=s
            if s<minm:
                minm=s
            rec(root.left,s-1)
            rec(root.right,s+1)
        
        rec(root,0)
        return [hs[i] for i in range(minm,maxm+1)]


    def levelOrderRec(self,root):
        hs={}
        minm,maxm=float("inf"),float("-inf")
        def rec(root,s):
            nonlocal minm,maxm
            if not root:
                return
            if s not in hs:
                hs[s]=[]
            hs[s].append(root.data)

            if s>maxm:
                maxm=s
            if s<minm:
                minm=s    

            rec(root.left,s+1)
            rec(root.right,s+1)

        rec(root,0)
        return [hs[i] for i in range(minm,maxm+1)]
        
        

    
sol=Solution()
#arr=[1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, None, 9]
arr=[1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16]
# arr=[46,2,47,1,28,None,72,None,None,11,43,54,79,8,12,29,44,53,55,73,83,7,10,None,23,None,40,None,45,49,None,None,63,None,77,81,92,5,None,9,None,14,25,39,42,None,None,48,51,58,69,74,78,80,82,88,95,4,6,None,None,13,21,24,27,31,None,41,None,None,None,50,52,57,59,64,70,None,75,None,None,None,None,None,None,85,91,94,99,3,None,None,None,None,None,15,22,None,None,26,None,30,35,None,None,None,None,None,None,56,None,None,62,None,67,None,71,None,76,84,87,89,None,93,None,97,100,None,None,None,19,None,None,None,None,None,None,33,37,None,None,61,None,66,68,None,None,None,None,None,None,86,None,None,90,None,None,96,98,None,None,18,20,32,34,36,38,60,None,65,None,None,None,None,None,None,None,None,None,None,None,17,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,16]
root=sol.build(arr)
#print(sol.verticalOrder2(root))
print(sol.levelOrderRec(root))