class Solution:
    # la solucion es desde atras hacia adelante
    # se crea un $ en la posicion y se avanza en las ramas
    # si determina el valor de dicha rama y se vuelve 
    # a establecer el valor de la posicion al valor original
    # de modo de continuar en ramas siguientes en caso de falso
    def isWordExist(self, mat, word):
        #Code here
        n,m=len(mat),len(mat[0])
        
        def dfs(i,j,k):
            if k==len(word):
                return True
            # poda
            if i<0 or i>=n or j<0 or j>=m or mat[i][j]!=word[k]:
                return False
            temp=mat[i][j]
            mat[i][j]='$'
            res=dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            # restablecimiento de valor
            mat[i][j]=temp
            return res

        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False
    
mat =[['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word = "GEEK"
sol=Solution()
print(sol.isWordExist(mat,word))
