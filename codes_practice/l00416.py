class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        target_value = sum(nums)
        if length == 1 or target_value % 2 == 1:
            return False
        target_value //= 2

        status = [0] * (target_value+1)
        for i in range(nums[0], target_value+1):
            status[i] = nums[0]

        for i in range(1, len(nums)):
            number = nums[i]
            for j in range(target_value, number-1, -1):
                status[j] = max(status[j - number]+number, status[j])

        return status[target_value] == target_value


s = Solution()
print(s.canPartition([1, 2, 5]))
