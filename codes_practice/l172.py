class Solution(object):
    def trailingZeroes(self, n):
        if n < 5:
            return 0
        factor = 5
        f_number = 0
        while factor <= n:
            f_number += n//factor
            factor = factor * 5
        return f_number


def main():
    s = Solution()
    print(s.trailingZeroes(30))


if __name__=='__main__':
    main()
     