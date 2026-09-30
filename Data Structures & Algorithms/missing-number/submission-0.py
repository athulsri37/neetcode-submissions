class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expSum = n*(n+1)/2
        actSum = sum(nums)
        return int(expSum - actSum)
        