
class Solution:
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        # Your code here
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        regions = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if mat[i][j] != 0:
                    rows[i].add(mat[i][j])
                    cols[j].add(mat[i][j])
                    regions[(i // 3) * 3 + (j // 3)].add(mat[i][j])

        def is_valid(i, j, val):
            return val not in rows[i] and val not in cols[j] and val not in regions[(i // 3) * 3 + (j // 3)]

        def place_value(mat,i, j, val):
            mat[i][j] = val
            rows[i].add(val)
            cols[j].add(val)
            regions[(i // 3) * 3 + (j // 3)].add(val)

        def remove_value(mat, i, j, val):
            mat[i][j] = 0
            rows[i].remove(val)
            cols[j].remove(val)
            regions[(i // 3) * 3 + (j // 3)].remove(val)

        def solve(mat):
            for i in range(9):
                for j in range(9):
                    if mat[i][j]==0:
                        for value in range(1,10):
                            if is_valid(i,j,value):
                                place_value(mat, i,j,value)
                                if solve(matrix):
                                    return True
                                else:
                                    remove_value(mat,i,j,value)
                        return False
            return True
        solve(matrix)

matrix= [
    [3, 0, 6, 5, 7, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 8, 6, 3, 0, 0]
]
sol=Solution()
sol.solveSudoku(matrix)
print(matrix)