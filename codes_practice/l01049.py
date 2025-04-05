class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        sum_weight = sum(stones)
        target_weight = sum_weight // 2

        s = [0] * (target_weight + 1)
        for i in range(stones[0], target_weight + 1):
            s[i] = stones[0]

        for j in range(1, n):
            cur_weight = stones[j]
            for i in range(target_weight, cur_weight - 1, -1):
                s[i] = max(s[i - cur_weight] + cur_weight, s[i])

        return sum_weight - s[-1] * 2


s = Solution()
print(s.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
