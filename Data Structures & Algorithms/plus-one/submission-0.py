class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        res = []
        for dig in digits:
            num = num*10 + dig
        num += 1
        while num > 0:
            rem = num %10
            res.append(rem)
            num = num // 10
       
        return res[::-1]
        