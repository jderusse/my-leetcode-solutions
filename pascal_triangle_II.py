class Solution:
    def getRow(self, rowIndex): 
        if rowIndex == 0:
           return [1]
    
        prevRow = [1]
        
        for i in range(rowIndex + 1):
            if (i == 0):
                continue
            
            rowSize = i + 1
            rowElements = [0] * rowSize
                      
            for j in range(rowSize):
                if j == 0 or j == rowSize - 1:
                    rowElements[j] = 1
                else:
                    rowElements[j] = prevRow[j] + prevRow[j - 1]
            
            if i == rowIndex:
                return rowElements
            
            prevRow = rowElements

        return None
