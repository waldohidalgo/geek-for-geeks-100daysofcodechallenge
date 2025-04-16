from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution():
    def cloneGraph(self, node):
        #code here
        if not node:
            return None
        queue = deque()
        original_map_clones={}
        original_map_clones[node]=Node(node.val)
        queue.append(node)
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in original_map_clones:
                    original_map_clones[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)
                original_map_clones[curr].neighbors.append(original_map_clones[neighbor])

        return original_map_clones[node]
    
    def cloneGraph2(self,node):
        map={}
        def dfs(node):
            if node in map:
                return map[node]
            clone=Node(node.val)
            map[node]=clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)    