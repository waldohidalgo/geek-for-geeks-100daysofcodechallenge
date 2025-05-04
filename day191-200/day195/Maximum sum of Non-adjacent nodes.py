from collections import deque
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:

    def buildTree(self,arr):
        q=deque()
        root=Node(arr[0])
        q.append(root)
        i=1
        while i<len(arr):
            parent=q.popleft()
            if arr[i]!=None:
                parent.left=Node(arr[i])
                q.append(parent.left)
            i+=1
            if i>=len(arr):
                break
            if arr[i]!=None:
                parent.right=Node(arr[i])
                q.append(parent.right)
            i+=1
        return root


    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self, root):
        #code here
        def dfs(node):
            if not node:
                return [0,0]
            
            left_include, left_exclude = dfs(node.left)
            right_include, right_exclude = dfs(node.right)
            
            include = node.data + left_exclude + right_exclude
            exclude = max(left_include, left_exclude) + max(right_include, right_exclude)
            
            return [include, exclude]
        
        include, exclude = dfs(root)
        
        return max(include, exclude)


sol=Solution()
arr = [1, 2, 3, 4, None, 5, 6]
root=sol.buildTree(arr)
print(sol.getMaxSum(root))