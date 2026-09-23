class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for letter in s:
            if letter.isalnum():
                newStr+=letter.lower()
        #print(newStr)
        i = 0
        j = len(newStr) - 1
        while i < len(newStr) and j > 0:
            if newStr[i] != newStr[j]:
                return False
            i+=1
            j-=1
        return True
        