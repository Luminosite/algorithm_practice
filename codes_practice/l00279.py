import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        element_size = int(math.sqrt(n))
        status = []
        for i in range(n+1):
            status.append(i)

        for i in range(2, element_size+1):
            num = i*i
            for j in range(num, n+1):
                status[j] = min(status[j-num]+1, status[j])
        return status[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(13))
