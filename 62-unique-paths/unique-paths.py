class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROW, COL = m, n
        def memo(m, n, cache):
            if m == ROW or n == COL:
                return 0
            if cache[m][n] > 0:
                return cache[m][n]
            if m == ROW - 1 and n == COL - 1:
                return 1
            cache[m][n] = memo(m + 1, n, cache) + memo(m, n + 1, cache)
            return cache[m][n]
        grid = [[0] * COL for i in range(ROW)]
        return memo(0,0,grid)

            

        