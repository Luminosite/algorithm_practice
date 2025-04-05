class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [2]
        base = ['1'] * n

        # i = 0
        ret = 0
        search_min = 3
        for i in range(2, n):
            if base[i] == '1':
                t = i*2
                while t < n:
                    base[t] = '0'
                    t += i
                ret += 1

        #     pi = primes[i]
        #     k = 2
        #     while pi * k < n:
        #         base[pi*k] = '0'
        #         k += 1
            
        #     search_max = min(2*pi, n)
        #     if search_min <= search_max:
        #         for j in range(search_min, search_max):
        #             if j<n and base[j] == '1':
        #                 primes.append(j)
        #         search_min = search_max
        #     i += 1


        # print(primes)
        # return len(primes)
        return ret
        

def main():
    s = Solution()
    print(s.countPrimes(1000))


if __name__=='__main__':
    main()
     