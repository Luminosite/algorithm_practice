class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 4:
            return max(nums)
        ret = 0
        status = [0] * n
        for i in range(1, n):
            t_2 = status[i - 2] if i >= 2 else 0
            t_3 = status[i - 3] if i >= 3 else 0
            status[i] = nums[i] + max(t_2, t_3)
            if status[i] > ret:
                ret = status[i]

        status = [0] * n
        for i in range(0, n-1):
            t_2 = status[i - 2] if i >= 2 else 0
            t_3 = status[i - 3] if i >= 3 else 0
            status[i] = nums[i] + max(t_2, t_3)
            if status[i] > ret:
                ret = status[i]
        return ret


s = Solution()
print(s.rob([1,2,3,1,9]))
