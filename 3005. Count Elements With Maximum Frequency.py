# Example 1:

# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# Example 2:

# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.




from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method: 1
        # s = set(nums)
        # cou = []
        # for i in s:
        #     cou = [nums.count(i) for i in s]

        # maximum = max(cou)

        # n = cou.count(maximum)
        # return maximum*n


        # Method: 2
        # s = set(nums)
        # cou = []
        # cou = Counter(nums)
        # # print("Cou is: ",cou)
        
        # maximum = max(cou.values())
        # # print('Max is: ',maximum)

        # res = Counter(cou.values())
        # # print("res is: ",res)

        # n = res[maximum]

        # return n * maximum







# nums = [1,2,2,3,1,4] # Output = 4
# nums = [1,2,3,4,5] # Output = 5
nums = [10,12,11,9,6,19,11] # Output = 2


solution = Solution()
print(solution.maxFrequencyElements(nums))