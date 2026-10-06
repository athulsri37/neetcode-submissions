class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        binary = bin(n)[2:]
        return binary.count('1')
        