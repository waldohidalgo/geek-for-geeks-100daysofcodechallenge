class Solution:
    def generateMatrix(self, rowSum, colSum):
        # code here
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]

        return matrix
    
sol=Solution()
rowSum = [1, 0]
colSum= [1]
print(sol.generateMatrix(rowSum,colSum))