class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        status = [0]*(n+1)
        status[0] = 1
        status[1] = 1
        if n > 1:
            status[2] = 2

        for i in range(3, n+1):
            for j in range(1, i+1):
                status[i] += status[j-1] * status[i-j]

        return status[-1]


s = Solution()
print(s.numTrees(2))
