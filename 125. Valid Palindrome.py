class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        
        clean_str = [c for c in s if c.isalnum()]

        clean_str = ''.join(clean_str)

        # print(clean_str[::-1])
        # print(clean_str)
        if clean_str[::-1] == clean_str:
            return True
        return False




s = "A man, a plan, a canal: Panama" # Output: True
# s = "race a car"  # Output: False


solution = Solution()
print(solution.isPalindrome(s))