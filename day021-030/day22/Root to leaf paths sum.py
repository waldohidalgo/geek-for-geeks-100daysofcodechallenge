from collections import deque
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class BinaryTree:

    def __init__(self, arr):
        self.root=self.buildTree(arr)

    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

    def buildTree(self, arr):
        if len(arr) == 0:
            return None
        root = Node(arr[0])
        q = deque()
        q.append(root)
        i = 1
        while i < len(arr):
            parent = q.popleft()
            if arr[i] != None:
                parent.left = Node(arr[i])
                q.append(parent.left)
            i += 1
            if i >= len(arr):
                break
            if arr[i] != None:
                parent.right = Node(arr[i])
                q.append(parent.right)
            i += 1
        return root
        

class Solution:
    def treePathSum(self,root):
        # Code here
        res=[]
        if not root:
            return 0
        def dfs(root,acumSum):
            if not root.left and not root.right:
                res.append(acumSum)
                return
            if root.left:
                dfs(root.left,acumSum*10+root.left.data)
            if root.right:
                dfs(root.right,acumSum*10+root.right.data)
        dfs(root,root.data)
        return sum(res)
    
    def treePathSum2(self,root):
        # Code here
        def dfs(root,acumSum):
            if not root.left and not root.right: 
                return acumSum
            total=0
            if root.left:
                total+=dfs(root.left,acumSum*10+root.left.data)
            if root.right:
                total+=dfs(root.right,acumSum*10+root.right.data) 
            return total
        return dfs(root,root.data) if root else 0
            
        

        
arr=[10,20,30,40,50,60]
bt=BinaryTree(arr)
root=bt.root
#bt.printTree(root)
ob=Solution()
print(ob.treePathSum2(root))

