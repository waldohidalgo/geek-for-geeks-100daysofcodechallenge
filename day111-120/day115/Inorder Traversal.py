
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
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

