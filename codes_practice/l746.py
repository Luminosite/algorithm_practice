class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        t_1=0
        t_2=0
        t = 0
        for i in range(2, n+1):
            t = min(t_1 + cost[i-1], t_2 + cost[i-2])
            t_2 = t_1
            t_1 = t
        return t

s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
