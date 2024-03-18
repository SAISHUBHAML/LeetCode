class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0
        for i in jewels:
            k = stones.count(i)
            res += k

        return res


jewels = "aA"
stones = "aAAbbbb"

s = Solution()
print(s.numJewelsInStones(jewels,stones))