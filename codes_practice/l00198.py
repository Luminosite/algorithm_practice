class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n >= 3:
            nums[2] += nums[0]
        if n < 4:
            return max(nums)
        ret = max(nums[1], nums[2])

        for i in range(3, n):
            nums[i] += max(nums[i - 2], nums[i - 3])
            if nums[i] > ret:
                ret = nums[i]
        return ret


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
