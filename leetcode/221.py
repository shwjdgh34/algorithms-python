class Solution(object):
    def maximalSquare(self, matrix):
        maximal = 0
        m = len(matrix)
        n = len(matrix[0])

        squreSizeMemo = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (matrix[i][j] == "1"):
                    squreSizeMemo[i][j] = min(squreSizeMemo[i+1][j], squreSizeMemo[i][j+1], squreSizeMemo[i+1][j+1]) + 1
                    if maximal < squreSizeMemo[i][j]: maximal = squreSizeMemo[i][j]
            

        return maximal*maximal
        


s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
