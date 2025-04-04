class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        status = [0] * n
        status[0] = 1
        for i in range(m):
            for j in range(0, n):
                if not (i == 0 and j == 0):
                    if obstacleGrid[i][j] == 0:
                        status[j] += status[j - 1] if j > 0 else 0
                    else:
                        status[j] = 0
        return status[-1]


s = Solution()
print(s.uniquePathsWithObstacles(
    [[0, 1], [0, 0]]
))
