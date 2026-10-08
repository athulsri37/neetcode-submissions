class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        freqSorted = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        return freqSorted[0][0]
        
        