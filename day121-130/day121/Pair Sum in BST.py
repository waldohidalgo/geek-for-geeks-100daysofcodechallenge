from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class IteratorCustom:
    def __init__(self, root, forward):
        self.stack = []
        self.forward = forward 
        self._push_nodes(root)

    def _push_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left if self.forward else node.right

    def next(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        if self.forward:
            self._push_nodes(node.right)
        else:
            self._push_nodes(node.left)
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
    def findTarget(self, root, tg): 
        # your code here.
        if not root:
            return False
        left_iterator=IteratorCustom(root,True)
        right_iterator=IteratorCustom(root,False)

        left_node=left_iterator.next()
        right_node=right_iterator.next()

        while left_node and right_node and left_node.data<right_node.data:
            curr=left_node.data+right_node.data
            if curr==target:
                return True
            if curr>target:
                right_node=right_iterator.next()
            else:
                left_node=left_iterator.next()
        return False

    

    def findTarget1(self, root, tg):
        self.exist=False
        def rec(root,hs):
            if not root or self.exist==True:
                return
            rec(root.left,hs)
            if self.exist:
                return
            if tg-root.data in hs:
                self.exist=True
                return
            hs.add(root.data)
            rec(root.right,hs)

        
        rec(root,set())
        return self.exist



# arr=[7, 3, 8, 2, 4, None, 9]
# target=12
# arr=[9, 5, 10, 2, 6, None, 12]
# target=23
# arr=[7,3,12,2,4,10,13]
# target=15
arr=[4,2,6,1,3,5,7]
target=5
sol=Solution()
root=sol._build(arr)
print(sol.findTarget1(root,target))

            
            


