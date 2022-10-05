class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i, j = 0, 0
        s = 0
        while i < len(mat):
            s += mat[i][j]
            i, j = i + 1, j + 1
        
        i, j = 0, len(mat) - 1
        while i < len(mat):
            s += mat[i][j]
            i, j = i + 1, j - 1
        
        if len(mat) % 2 == 1:
            center = mat[len(mat) // 2][len(mat) // 2]
            return s - center
        return s
        