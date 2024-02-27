# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

# Example 1:
# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.

# Example 2:
# Input: operations = ["++X","++X","X++"]
# Output: 3
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# ++X: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# X++: X is incremented by 1, X = 2 + 1 = 3.

# Example 3:
# Input: operations = ["X++","++X","--X","X--"]
# Output: 0
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# X++: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# --X: X is decremented by 1, X = 2 - 1 = 1.
# X--: X is decremented by 1, X = 1 - 1 = 0.
 

# Constraints:
# 1 <= operations.length <= 100
# operations[i] will be either "++X", "X++", "--X", or "X--".


class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        p_count = 0
        n_count = 0
        for i in operations:
            if i[1] == "-":
                n_count += 1
            else:
                p_count += 1

        # print("n_count is: ",n_count)
        # print("p_count is: ",p_count)
        k = 0 - n_count + p_count
        return k















operations = ["--X","X++","X++"] #1
# operations = ["++X","++X","X++"] #3
# operations = ["X++","++X","--X","X--"] #0




solution = Solution()
print(solution.finalValueAfterOperations(operations))





































