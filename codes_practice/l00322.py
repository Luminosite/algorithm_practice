class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        status = [-1] * (amount + 1)
        status[0] = 0

        for c in coins:
            for j in range(c, amount + 1):
                if status[j - c] != -1:
                    if status[j] == -1:
                        status[j] = status[j - c] + 1
                    else:
                        status[j] = min(status[j - c] + 1, status[j])
        return status[-1]


s = Solution()
print(s.coinChange( [2,1], 0 ))
