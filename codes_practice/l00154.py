class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length>1:
            if nums[0] < nums[-1]:
                return nums[0]
            else: # nums0 >= numsN
                if length == 2:
                    return nums[-1]
                mid = (length-1)//2
                if nums[mid] > nums[0]:
                    return self.findMin(nums[mid+1:])
                elif nums[mid] < nums[-1]:
                    return self.findMin(nums[:mid+1])
                # 0 >= mid >= N
                else:
#                     print(nums[:mid], nums[mid+1:])
                    return min(self.findMin(nums[:mid]), self.findMin(nums[mid+1:]))
        else:
            return nums[0]

s = Solution()
print("final:", s.findMin([4,4,4,4,4,1,4]))
