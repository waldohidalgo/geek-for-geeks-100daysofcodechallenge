from collections import defaultdict, deque
class Solution:
    def findOrder(self,words):
        adj = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""  

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break  

        q = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while q:
            char = q.popleft()
            result.append(char)

            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        
        if len(result) < len(in_degree):
            return ""

        return "".join(result)
    
    def findOrder2(self,words):
        adj = defaultdict(set)
        all_chars = set(''.join(words)) 
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""  

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                    break

        # usar dfs para encontrar el orden topológico

        visited =  {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]  
            visited[c] = False 
            for nei in adj[c]:
                if not dfs(nei):
                    return False # Ciclo detectado
            visited[c] = True  
            res.append(c)
            return True

        for c in all_chars:
            if c not in visited:
                if not dfs(c):
                    return ""  # Ciclo detectado

        return ''.join(reversed(res))
        

sol=Solution()
#words= ["baa", "abcd", "abca", "cab", "cad"]
words=["cc","ccac","bd","bacc","d","dda","a","aca","abdaa"]
print(sol.findOrder(words))
#print(sol.findOrder2(words))
