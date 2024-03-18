# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]
 
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.



class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        lst = []
        res = []
        self.func(0, s, lst, res)
        return res

    def func(self, partition, s, lst, res):
        if partition == len(s):
            # print("I am in the if cond")
            res.append(lst[:])
            return

        for i in range(partition, len(s)):
            if self.is_palindrome(s, partition, i):
                lst.append(s[partition : i + 1])
                # print("lst is: ",lst)
                self.func(i + 1, s, lst, res)
                lst.pop()
                # print("lst.pop() = ", lst.pop())
        

    def is_palindrome(self, s, i, j):
        k = s[i:j+1]
        if k[::-1] == k:
            return True
        else: 
            return False







s = "aab" # Output: [["a","a","b"],["aa","b"]]
# s = "a" # Output: [["a"]]



solution = Solution()
print(solution.partition(s))




# for each palindrome substring in the string
# dic = {}
# for i in range(0,len(s)):
#     # lst = []
#     for j in range(i,len(s)):
#         k = s[i:j+1]
#         if len(k) not in dic:
#             dic[len(k)] = []
        
#         # print("The value of k is: ",k)
#         if k == k[::-1]:
#             # lst.append(k)
#             dic[len(k)].append(k)
#     # print(lst)

# # print("The dic is: ",dic)
# lst = [dic[i] for i in dic if len(dic[i]) >0 ]

# return lst