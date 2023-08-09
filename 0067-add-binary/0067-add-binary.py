class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bin_data = bin(int(a, 2) + int(b, 2))
        return str(bin_data[2:])
        