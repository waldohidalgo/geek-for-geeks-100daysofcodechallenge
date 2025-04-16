from collections import defaultdict,deque
from typing import List

class Solution:
    def accountsMerge(self, accounts):
        # Code here

        # cada email es un nodo y toda acc con mismos emails tiene el mismo nombre
        email_graph = defaultdict(list)
        email_to_name = {}
        

        for acc in accounts:
            n=len(acc)
            name = acc[0]
            first_email = acc[1]
            for i in range(1,n):
                email=acc[i]
                email_graph[first_email].append(email)
                email_graph[email].append(first_email)
                if email not in email_to_name:
                    email_to_name[email] = name

        visited = set()
        result = []

        def dfs(email, component: List[str]):
            visited.add(email)
            component.append(email)
            for neighbor in email_graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for email in email_graph:
            if email not in visited:
                component = []
                dfs(email, component)
                result.append([email_to_name[email]] + sorted(component))

        return result
    
    def accountsMerge2(self, accounts):
        
        email_graph = defaultdict(list)
        email_to_name = {}        
        for acc in accounts:
            n=len(acc)
            name = acc[0]
            first_email = acc[1]
            for i in range(1,n):
                email=acc[i]
                email_graph[first_email].append(email)
                email_graph[email].append(first_email)
                if email not in email_to_name:
                    email_to_name[email] = name

        visited = set()
        result = []


        def bfs(email_input,component: List[str]):
            q=deque([email_input])
            while q:
                email=q.popleft()
                if email in visited: # linea clave en este enfoque bfs
                    continue
                visited.add(email)
                component.append(email)
                for neighbor in email_graph[email]:
                    if neighbor not in visited:
                        q.append(neighbor)                


        for email in email_graph:
            if email not in visited:
                component = []
                bfs(email,component)
                result.append([email_to_name[email]] + sorted(component))

        return result






# accounts =[
# ["John","johnsmith@mail.com","john_newyork@mail.com"],
# ["John","johnsmith@mail.com","john00@mail.com"],
# ["Mary","mary@mail.com"],
# ["John","johnnybravo@mail.com"]]
# accounts=[
# ["Gabe","Gabe00@m.co","Gabe3@m.co","Gabe1@m.co"],
# ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
# ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
# ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
# ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
accounts = [
    ["mark", "mark2@gmail.com"],
    ["alice", "alice2@mail.com", "alice9@google.in", "alice6gfg.org"],
    ["fern", "fern9gfg.org", "fern3@mail.com", "fern3@mail.com", "fern7gfg.org", "fern2gfg.org", "fern8@mail.com"],
    ["kevin", "kevin0gfg.org", "kevin3@mail.com", "kevin2@gmail.com", "kevin8@gmail.com", "kevin8@mail.com"],
    ["kevin", "kevin1@gmail.com", "kevin6@google.in", "kevin6@google.in", "kevin2@mail.com", "kevin7@google.in", "kevin5@gmail.com", "kevin9gfg.org"],
    ["bob", "bob3@gmail.com", "bob4@mail.com"]
]
sol=Solution()
print(sol.accountsMerge(accounts))
print("\n")
print(sol.accountsMerge2(accounts))