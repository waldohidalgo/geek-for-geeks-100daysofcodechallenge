from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class IteratorCustom:
    def __init__(self, root):
        self.stack = []
        self._push_nodes(root)

    def _push_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        self._push_nodes(node.right)
        return node

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
    
    def _show(self,root):
        res=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            for _ in range(n):
                node=queue.popleft()
                res.append(node.data if node else None)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        while res[-1] is None:
            res=res[:-1]
        print(res)  
    
    def correctBST(self, root):
    # your code here
        first=None
        first_next=None
        second=None
        prev_node=Node(float("-inf"))
        def inorder(root):
            nonlocal prev_node,first,first_next,second
            if not root or second:
                return
            inorder(root.left)
            if second:
                return
            if prev_node.data>root.data:
                if not first:
                    first=prev_node
                    first_next=root
                else:
                    second=root
            prev_node=root
            inorder(root.right)

        inorder(root)
        if not second:
            first.data,first_next.data=first_next.data,first.data
        else:
            first.data,second.data=second.data,first.data

    def correctBST1(self,root):
        iterator_tree=IteratorCustom(root)
        first=None
        first_next=None
        second=None
        prev_node=Node(float("-inf"))
        curr_node=iterator_tree.next()
        while curr_node:
            if second:
                break
            if prev_node.data>curr_node.data:
                if not first:
                    first=prev_node
                    first_next=curr_node
                else:
                    second=curr_node
            prev_node=curr_node
            curr_node=iterator_tree.next()
        if not second:
            first.data,first_next.data=first_next.data,first.data
        else:
            first.data,second.data=second.data,first.data
        
        


sol=Solution()
arr=[5, 10, 20, 2, 8]
root=sol._build(arr)
sol.correctBST(root)
sol._show(root)

        


            