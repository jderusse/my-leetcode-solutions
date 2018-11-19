class Solution:
    def isPalindrome(self, x):
        indexedNumber = str(x)
        if indexedNumber[0] == "-":
            return False
        
        numSize = len(indexedNumber)
        
        for i in range(numSize):
            oppositeIndex = numSize - 1 - i
            
            if (oppositeIndex == i):
                break
            
            if indexedNumber[i] != indexedNumber[oppositeIndex]:
                return False
        
        return True