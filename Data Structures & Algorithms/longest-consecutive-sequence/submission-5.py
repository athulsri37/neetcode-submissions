class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        res = 1
        maxRes = 1
        for i in range(len(nums)-1):
            if abs(nums[i+1] - nums[i]) == 1:
                res += 1
                maxRes = max(maxRes,res) 
            else:
                res = 1
        print(maxRes)    
        return maxRes
        