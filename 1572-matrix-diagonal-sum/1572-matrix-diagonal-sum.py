class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        for i in range(n):
            s += mat[i][i] + mat[i][n - i -1]
            i += 1
        
        center = mat[n // 2][n // 2]
        return s if len(mat) % 2 == 0 else s - center
        