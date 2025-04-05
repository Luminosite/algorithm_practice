class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # build diction
        size = len(s)
        diction = {}
        for word in wordDict:
            d = diction
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['stop'] = ''

        status = [False] * size

        for i in range(size):
            if i == 0 or status[i - 1]:
                check_dict = diction
                j = i
                while j < size and s[j] in check_dict:
                    check_dict = check_dict[s[j]]
                    if 'stop' in check_dict:
                        status[j] = True
                    j = j + 1
        return status[-1]


s = Solution()
print(s.wordBreak("a", ['b']))
