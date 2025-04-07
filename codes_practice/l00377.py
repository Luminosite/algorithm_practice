class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        status = [0]*(target+1)
        status[0] = 1

        # this is solution for finding charge.
        # when travel on statue, charge's order is fixed, and is same as order in nums
        # in this way, we got combination number
        # for example, nums is [1,2] and target=4, it only generates 1,1,2. but never 1,2,1 or 2,1,1
        # for i in nums:
        #     for j in range(i, target+1):
        #         status[j] += status[j-i]
        # return status[-1]

        # in 377, to consider all different sequences
        # travel nums in the travel of status.
        for j in range(1, target+1):
            for i in nums:
                if i <= j:
                    status[j] += status[j-i]
        return status[-1]


s = Solution()
print(s.combinationSum4(
    [1,2,3],
    4
))

