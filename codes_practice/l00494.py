class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        sum_value = sum(nums)
        tmp_t = (sum_value - target)
        if tmp_t < 0:
            return 0
        if tmp_t % 2 == 1:
            return 0
        t = tmp_t // 2
        s = [0] * (t + 1)
        counts = ([1] if nums[0] != 0 else [2]) * (t + 1)

        for i in range(nums[0], t + 1):
            s[i] = nums[0]

        for i in range(1, n):
            number = nums[i]
            for j in range(t, number - 1, -1):
                cur_v = s[j]
                cur_v_j = s[j - number] + number
                if cur_v > cur_v_j:
                    s[j] = cur_v
                elif cur_v < cur_v_j:
                    s[j] = cur_v_j
                    counts[j] = counts[j - number]
                else:
                    counts[j] = counts[j] + counts[j - number]

        return counts[-1] if s[t] == t else 0


sol = Solution()
print(sol.findTargetSumWays(
    [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53],
    1000
))
