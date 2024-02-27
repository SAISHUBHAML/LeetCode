# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 

# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c_list = []
        uniq = set(arr)
        # print("Uniq is: ",uniq)
        for i in uniq:
            k = arr.count(i)
            # print("The value of K is: ",k)
            if k in c_list:
                return False
            c_list.append(k)
            # print("c_list is: ",c_list)
        return True












arr = [1,2,2,1,1,3] #True
# arr = [1,2] #False
# arr = [-3,0,1,-3,1,1,1,-3,10,0] #True


solution = Solution()
print(solution.uniqueOccurrences(arr))






