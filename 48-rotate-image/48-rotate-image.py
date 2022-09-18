class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = math.ceil(m/2)
        for i in range(n):
            for j in range(m//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[m-j-1][i]
                matrix[m-j-1][i] = matrix[m-i-1][m-j-1]
                matrix[m-i-1][m-j-1] = matrix[j][m-i-1]
                matrix[j][m-i-1] = temp