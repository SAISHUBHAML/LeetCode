# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """              
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             if nums[i] + nums[j] == target:
        #                 return [i,j]



        # for i in range(len(nums)):
        #     if i != len(nums):
        #         k = i+1
        #     else:
        #         k = i
        #     for k in range(i+1,len(nums)):
        #         if nums[i] + nums[k] == target:
        #             return [i,k]


        # # Using Dictionary concept
        # numToIndex = {}
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in numToIndex:
        #         return [numToIndex[complement], i]
        #     numToIndex[num] = i

        numsWithIndex = [(num, i) for i, num in enumerate(nums)]
        numsWithIndex.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            num_sum = numsWithIndex[left][0] + numsWithIndex[right][0]
            if num_sum == target:
                return [numsWithIndex[left][1], numsWithIndex[right][1]]
            elif num_sum < target:
                left += 1
            else:
                right -= 1
                    











# nums, target = [2,7,11,15],9 # output = [0,1]
nums, target = [3,2,4],6 # output = [1,2]
# nums, target = [3,3],6 # output = [0,1]
# nums, target = [3,2,4],6


solution = Solution()
print(solution.twoSum(nums,target))






















































