'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    #Your Function check Completeness and Max-Heap Property
    def isHeap(self, root):
        # code Here
        queue = deque([root])
        end = False  

        while queue:
            node = queue.popleft()
            
            if node.left:
                if end or node.data < node.left.data:
                    return False
                queue.append(node.left)
            else:
                end = True

            if node.right:
                if end or node.data < node.right.data:
                    return False
                queue.append(node.right)
            else:
                end = True
        
        return True