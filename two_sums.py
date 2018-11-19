class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            
            try:
                complementIdx = nums.index(complement)
            except:
                continue
            
            if i == complementIdx:
                continue
            
            return [i, complementIdx]
        
        return None