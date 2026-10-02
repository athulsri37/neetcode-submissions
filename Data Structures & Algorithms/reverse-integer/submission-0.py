class Solution:
    def reverse(self, x: int) -> int:
        print(pow(2,31))
        neg = x < 0
        x = abs(x)
        num = 0
        while x>0:
            rem = x%10
            num = num*10 + rem
            x = x//10
            #print(x, rem, num)
        if neg:
            num = -num
        if num < pow(-2,31) or  num > pow(2,31) - 1:
            return 0
        return num


        