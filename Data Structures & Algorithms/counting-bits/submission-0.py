class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = []
        for i in range(n+1):
            num = bin(i)[2:]
            ones.append(self.returnOnes(num))
            
        return ones

    def returnOnes(self, num: str) -> int:
        res = 0
        for ch in num:
            if ch == '1':
                res+=1
        return res
        