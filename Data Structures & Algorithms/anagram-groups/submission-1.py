class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sortedStrs = {}
        for i in range(len(strs)):
            sortedStr = "".join(sorted(strs[i]))
            if sortedStr in sortedStrs:
                pos = sortedStrs[sortedStr]
                pos.append(i)
                sortedStrs[sortedStr] = pos
            else:
                sortedStrs[sortedStr] = [i]
        for item in sortedStrs.values():
            subList = []
            for pos in item:
                subList.append(strs[pos])
            res.append(subList)
                    
        return res
        