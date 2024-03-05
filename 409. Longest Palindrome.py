# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        setis = set(s)
        # print(setis)
        count_lst = []

        for i in setis:
            count_lst.append(s.count(i))
        
        # print("Count_lst is: ",count_lst)

        even = [value for value in count_lst if value % 2 == 0]
        odd = [value for value in count_lst if value % 2 != 0]

        # print(even, odd)
        # res_from_odd = [i for i in odd if i-1]
        res_from_odd = [i-1 for i in odd]
        # print("res_from_odd is: ",res_from_odd)
        result = sum(even) + sum(res_from_odd)
        
        if odd == []:
            return result
        else:
            return result + 1












# s = "abccccdd" # Output = 7
# s = "a" # Output = 1
# s = "bb" # Output = 2
s = "ccc" # Output = 3
# s = "bananas" #Output = 5


solution = Solution()
print(solution.longestPalindrome(s))

























