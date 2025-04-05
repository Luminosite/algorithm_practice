class Solution(object):

    @staticmethod
    def count01(str_val):
        zeros = 0
        ones = 0
        for c in str_val:
            if c == '0':
                zeros += 1
            else:
                ones += 1
        return zeros, ones

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        if not strs:
            return 0

        status = []
        for i in range(0, m + 1):
            status.append([0] * (n + 1))

        for k in range(0, len(strs)):
            z, o = Solution.count01(strs[k])
            for i in range(m, z-1, -1):
                for j in range(n, o-1, -1):
                    status[i][j] = max(
                        status[i-z][j-o] + 1,
                        status[i][j]
                    )
        return status[m][n]


s = Solution()
print(s.findMaxForm(
    ["", "10","0001","", "111001","1","0"],
    0,
    0))

