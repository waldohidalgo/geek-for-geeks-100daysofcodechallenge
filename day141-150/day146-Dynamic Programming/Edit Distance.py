class Solution:
    def editDistance(self, s1, s2):
		# Code here
        m, n = len(s1), len(s2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] 
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,  # Eliminar de s1
                                dp[i][j - 1] + 1,  # Insertar en s1
                                dp[i - 1][j - 1] + 1)  # Reemplazar
        
        return dp[m][n]

    def editDistance2(self, s1, s2):
		# Code here
        m, n = len(s1), len(s2)
        
        prev = [0] * (n + 1)
        curr=[0] * (n + 1)

        for j in range(n + 1):
            prev[j] = j # se insertan todos en s1
        
        for i in range(1, m + 1):
            curr[0]=i
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] 
                else:
                    curr[j] = min(prev[j] + 1,  # Eliminar de s1
                                curr[j - 1] + 1,  # Insertar en s1
                                prev[j - 1] + 1)  # Reemplazar
            prev=curr[:] # copio el curr porque solo usar curr las referencias se mantienen
        return curr[n]   

sol=Solution()
s1 = "abcd"
s2 = "bcfe"
print(sol.editDistance(s1,s2))
print(sol.editDistance2(s1,s2))