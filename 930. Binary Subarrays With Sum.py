

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        # # M3thod - 01 (Time Limit Exceeded)
        # i, j = 0, 0
        # res = 0
        # while j < len(nums):
        #     sum_is = sum(nums[i:j + 1])
        #     # print(i,j)
        #     if sum_is == goal:
        #         # print(nums[i:j+1],' ',sum_is)
        #         res += 1
        #         # print(res)
        #         k = i
        #         while k < j and nums[k] == 0:
        #             # print('considered array: ',nums[k+1:j+1])
        #             res += 1
        #             k += 1
        #         # print('res after compression: ',res)
        #         j += 1
        #     elif sum_is > goal:
        #         if i == j:
        #             j += 1
        #         else:
        #             i += 1
        #     else:
        #         j += 1
        # return res


        res = 0
        count = {0: 1}
        cur_sum = 0
        
        for i in nums:
            cur_sum += i
            if cur_sum - goal in count:
                res += count[cur_sum - goal]
            count[cur_sum] = count.get(cur_sum, 0) + 1

        return res








nums,goal = [1,0,1,0,1], 2

nums, goal = [0,0,0,0,0],0
    
nums,goal = [0,0,0,0,0,0,1,0,0,0], 0

# nums,goal = [0,0,0,0,0,0],0
s = Solution()
print(s.numSubarraysWithSum(nums,goal))







# cs-reply@amazon.in































