class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        status = [1] * (n + 1)

        for element in range(2, n):
            # Error!
            # for j in range(element, n+1):
            #     status[j] = max(status[j-element]*element, status[j])
            for j in range(element+1, n+1):
                status[j] = max(status[j-element]*element, status[j], element*(j-element))

        return status[-1]


s = Solution()
print(s.integerBreak(10))
