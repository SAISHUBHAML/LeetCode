class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i, j, z, res = 0, 0, len(nums), 0
        maximum = max(nums)
        freq = 0
        while j < z:
            print(f'j is {j}')
            if nums[j] == maximum:
                print('i am in if')
                freq += 1
                if freq >= k:
                    print('res added')
                    res = res + (z-j)
                    while nums[i] != maximum:
                        i += 1
                        res = res + (z-j)


                j += 1
            else:
                j += 1
            print(res)
                



























        # while j < z:
        #     if j < z and nums[j] == maximum:
        #         freq += 1
        #         j += 1

        #     while freq >= k:
        #         res += (z - j + 1)  # Updated the logic for counting occurrences
        #         if nums[i] == maximum:
        #             freq -= 1
        #         i += 1

        #     j += 1

        # return res





        # i,j,z,res = 0,0,len(nums),0
        # maximum = max(nums) # 3
        # while j < z:
        #     freq = 0
        #     if nums[j] == maximum:
        #         freq += 1
            

        #     while freq == k:
        #         res = res + (z - j)
        #         print('curr res is ',res)
        #         if nums[i] == maximum:
        #             freq -= 1

        #         i += 1

        #     j += 1

        # return res





nums, k = [1,3,2,3,3], 2

s = Solution()
print(s.countSubarrays(nums,k))






































