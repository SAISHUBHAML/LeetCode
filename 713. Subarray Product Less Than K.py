class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i,j = 0,len(nums)-1
        # return i,j
    
        res = 0
        pro = 1
        left = 0
        for a,b in enumerate(nums):
            pro *= b

            while pro >= k:
                pro /= nums[left]
                left += 1
            

            res += (a-left)+1

        return res










nums,k = [10,5,2,6], 100

s = Solution()
print(s.numSubarrayProductLessThanK(nums,k))









        