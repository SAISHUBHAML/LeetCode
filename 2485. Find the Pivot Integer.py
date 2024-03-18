# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.


class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1,n
        left = i
        right = n
        while i <= j:
            if i == j and left == right:
                return i
            else:
                if left < right:
                    i += 1
                    left += i
                else:
                    j -= 1
                    right += j
        return -1









n = 8
# n = 1
# n = 4

s = Solution()
print(s.pivotInteger(n))























