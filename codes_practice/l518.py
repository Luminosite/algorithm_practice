class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        status = [0] * (amount+1)
        status[0] = 1

        for c in coins:
            for i in range(c, amount+1):
                status[i] += status[i-c]
        return status[-1]


s = Solution()
print(s.change(3, [2]))
