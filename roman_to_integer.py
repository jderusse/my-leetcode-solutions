class Solution:
    def should_subtract(self, s, i):
        cur_val = s[i]
        next_val = s[i+1]
        
        return (cur_val == "I" and (next_val == "V" or next_val == "X")) or (cur_val == "X" and (next_val == "L" or next_val == "C")) or (cur_val == "C" and (next_val == "D" or next_val == "M"))
    
    def romanToInt(self, s):
        romanNumValueMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        value = 0;
        pass_next_iter = False
        
        for i in range(len(s)):
            if pass_next_iter:
                pass_next_iter = False
                continue
            
            try:
                nextRomVal = s[i+1]
            except:
                nextRomVal = None
            
            if None != nextRomVal and self.should_subtract(s, i):
                value += romanNumValueMap[s[i+1]] - romanNumValueMap[s[i]]
                pass_next_iter = True
                continue
                
            value += romanNumValueMap[s[i]]
        
        return value