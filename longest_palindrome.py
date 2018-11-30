class Solution:
    def longestPalindrome(self, s):
        charCountMap = {}
        for i in range(len(s)):
            if s[i] in charCountMap:
                charCountMap[s[i]] += 1
            else:
                charCountMap[s[i]] = 1
        
        additionalCharUsed = False
        longestPalindromeCount = 0
        
        for char, count in charCountMap.items():
            if count == 1 and False == additionalCharUsed:
                longestPalindromeCount += 1
                additionalCharUsed = True
                continue
            
            if count % 2 == 0:
                longestPalindromeCount += count
            else:
                longestPalindromeCount += (count - 1)
                
                if False == additionalCharUsed:
                    longestPalindromeCount += 1
                    additionalCharUsed = True
        
        return longestPalindromeCount
