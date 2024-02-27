# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # prefix = []
        # prefix.append(nums[0])
        # for i in range(1,len(nums)):
        #     k = prefix[i-1] + nums[i]
        #     prefix.append(k)
        # # print(nums)
        # # max_sum = prefix[0]
        # max_sum = sum(nums)
        # for i in range(0,len(nums)):
        #     print("prefix array is: ",prefix)
        #     print("nums is: ",nums)
        #     for j in range(0,len(nums)):
        #         print(prefix[j],prefix[i-1]) 
        #         curr_sum = prefix[0] if i == 0 else prefix[j] - prefix[i-1]
        #         if max_sum < curr_sum:
        #             max_sum = curr_sum
        #         print("curr_summ is: ",curr_sum)
        #     print("max sum is: ",max_sum)
        #     print("\n\n")
        # # print(prefix)
        # # print(max_sum)
        # return max_sum
        max_sum = float('-inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum







nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
# nums = [-2,-1]


solution = Solution()
print(solution.maxSubArray(nums))


























