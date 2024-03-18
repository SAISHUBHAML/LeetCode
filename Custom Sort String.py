# Example 1:
# Input:  order = "cba", s = "abcd" 
# Output:  "cbad" 
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.


# Example 2:
# Input:  order = "bcafg", s = "abcd" 
# Output:  "bcad" 
# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.


from collections import Counter
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        k = Counter(s)
        print(k)
        # To delete an element in dictionary
        # del k['a']

        print(k)
        print(k['a'])
        res = []
        for i in order:
            n = k[i]
            while n != 0:
                n -= 1
                # res.join(i)
                res.append(i)
            del k[i]
        
        
        if len(k) != 0:
            for i in k:
                # res.join(i)
                n = k[i]
                while n != 0:
                    n -= 1
                    res.append(i)
        res = ''.join(res)
        # print('res is: ',res)
        return res













# order, s = "cba", "abcd"
# order, s = "bcafg", "abcd"
order, s = "hucw", "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh" # Output = "hhhhhuucccwaaaaaaaaabbdddddeffffggggiijjjjkkkkllllmmmmnnnoooopppqqqqqqqqqqqrsssttttttttvxxxxxyyzzzzz"


solution = Solution()
print(solution.customSortString(order, s))













































