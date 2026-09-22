class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        freqSorted = dict(
            sorted(freq.items(), key=lambda x:x[1], reverse=True))
        res = list(freqSorted.keys())
        return res[:k]

        