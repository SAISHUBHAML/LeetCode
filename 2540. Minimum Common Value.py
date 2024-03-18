# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.

# Example 2:
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.



from collections import Counter
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        #Method - 01
        # n1  = sorted(set(nums1))
        # n2 = set(nums2)
        # n2_dic = Counter(n2)
        # print(n2_dic)
        # for i in n1:
        #     if n2_dic[i] > 0:
        #         return i
        #     else:
        #         continue
        # return -1


        # Method - 02
        # n1 = sorted(set(nums1))
        # n2 = sorted(set(nums2))
        # i,j = 0,0
        # while i<len(n1) and j < len(n2):
        #     if n1[i] == n2[j]:
        #         return n1[i]
        #     elif n1[i] > n2[j]:
        #         j += 1
        #     elif n1[i] < n2[j]:
        #         i += 1

        # return -1


        # Method - 03
        n1 = set(nums1)
        n2 = set(nums2)
        n2 = (n1 & n2)
        if len(n2) > 0 :
            return n2[0]
        else:
            return -1












# nums1, nums2 = [1,2,3], [2,4]
# nums1, nums2 = [1,2,3,6], [2,3,4,5]
# nums1, nums2 = [1,2,8,12,32,34,43,52,57,62,64,67,71,71,79,81,86,91,93,94], [9,11,12,14,19,25,29,31,38,39,41,42,58,63,66,70,71,73,91,91]
nums1, nums2 = [1,2,3],[4,5,6]
nums1, nums2 = [5,15,16,20,22,39,43,44,44,55,61,62,62,64,72,73,81,88,90,95], [2,8,9,11,12,13,26,29,38,49,50,51,58,63,67,72,75,82,92,96]

solution = Solution()
print(solution.getCommon(nums1, nums2))
















