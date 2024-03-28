class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        address = address.replace('.','[.]')
        
        return address




address = '1.1.1.1'

s = Solution()
print(s.defangIPaddr(address))