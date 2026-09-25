class Solution:
    def isValid(self, s: str) -> bool:
        match = {'[' : ']','(' : ')', '{' : '}'}
        res = []
        for item in s:
            if item in match:
                print("first = ", item)
                res.append(item)
            else:
                if len(res) == 0:
                    return False
                top = res[-1]
                print(top, match[top], item, item == match[top])
                if item == match[top]:
                    res.pop()
                else:
                    return False
        print("final=",res, len(res))
        return len(res) == 0

        