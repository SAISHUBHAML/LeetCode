from collections import defaultdict
class Solution:
    def numberofSubarrays(self, nums, k):
        'hi'
        dic = defaultdict(int)
        dic[0] = 1
        count, res = 0, 0
        for i in nums:
            if i % 2 != 0:
                count += 1
            if count >= k:
                res += dic[count-k]
            dic[count] += 1
        print(dic)
        return res



nums, k = [1, 1, 2, 1, 1], 3
# nums, k = [3, 2, 1, 0, 5], 1
# nums, k = [2, 4, 6], 1
s = Solution()
print(s.numberofSubarrays(nums, 3))