class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = []
        left_max.append(height[0])
        max = height[0]
        max_right = height[-1]
        # print(max_right)
        right_max = []
        for i in range(1,len(height)):
            if height[i] > max:
                max = height[i]
                left_max.append(max)
            else:
                left_max.append(max)

            if height[-i] > max_right:
                max_right = height[-i]
                right_max.append(max_right)
            else:
                right_max.append(max_right)
        if height[0] > max_right:
            right_max.append(height[0])
        else:
            right_max.append(max_right)


        right_max = right_max[::-1]    
        print(height )
        print(left_max)
        print(right_max)
        print("\n\n")
        
        
        trappedwater = 0
        for i in range(0,len(height)):
            print("the value of i is: ",i)
            water_level = min(left_max[i],right_max[i])
            print("Min of both is: ",water_level)
            trappedwater += water_level-height[i]
            print("Current trappedwater is: ",trappedwater)
            print("\n\n")
        # right_max = right_max[::-1]
        return trappedwater










# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,6,3,2,5]

solution = Solution()
print(solution.trap(height))

