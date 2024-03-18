# https://leetcode.com/problems/palindromic-substrings/

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Method: 1
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         k = s[i:j+1]
        #         if k == k[::-1]:
        #             count += 1
        
        # return count



        #Method: 2
        # n = set()
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         k = s[i:j+1]
        #         if k in n:
        #             count +=1
        #         else:
        #             if k == k[::-1]:
        #                 n.add(k)
        #                 count += 1
        
        # return count

        res = 0
        for i in range(len(s)):
            left = right = i
            # for n in range(0,len(s)-1):
            while left >= 0 and right < len(s) and s[left] == s[right]:

                # k = s[l:r+1]
                # if k == k[::-1]:
                #     print("The palin substr is: ",k)
                #     res +=1
                # else:
                #     break
                res += 1
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res
    







s = "aaa"


solution = Solution()
print(solution.countSubstrings(s))














