class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        
        curr = intervals[0]
        ret = []

        for i in intervals[1:]:
            if curr[1] >= i[0]:
                curr[1] = i[1]
            else:
                ret.append(curr)
                curr = i
        
        ret.append(curr)
        return ret
        

def main():
    a = [[1,3],[2,6],[8,10],[15,18]]
    s = Solution()
    print(s.merge(a))


if __name__=='__main__':
    main()