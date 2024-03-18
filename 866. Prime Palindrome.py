import math
class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 2
        


        def isprime(self, n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False

            for i in range(2,int(n**0.5) +1):
                if n % i != 0:
                    continue
                else:
                    return False
            return True
        
        # def is_palindrome(n):
        #     reversed_n = 0
        #     original_n = n
        #     while n > 0:
        #         reversed_n = reversed_n * 10 + n % 10
        #         n //= 10
        #     return original_n == reversed_n


        while True:
            # if str(n)[0] == str(n)[-1] and is_palindrome(n) and isprime(self, n) :
            # if n % 2 != 0 and is_palindrome(n) and isprime(self,n):
            if str(n)[0] == str(n)[-1] and str(n) == str(n)[::-1] and isprime(self,n):
                return n
            else:
                n += 1









n = 6 # Output = 7
# n = 13 # Output = 101
# n = 1 # Output = 2
# n = 9932400
# n = 9989900
n = 2 # Output = 3


solution = Solution()
print(solution.primePalindrome(n))