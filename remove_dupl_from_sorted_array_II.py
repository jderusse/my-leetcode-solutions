class Solution:
    def removeDuplicates(self, nums):
        currentSuccession = 0
        
        for key, num in enumerate(nums):
            if key == 0:
                currentSuccession += 1
                continue

            if key == len(nums) - 1 and currentSuccession >= 2 and num == nums[key - 1]:
                toDeleteCount = currentSuccession - 1
                for i in range(1, toDeleteCount + 1):
                    nums[key - i] = None

            if num != nums[key - 1]:
                if currentSuccession > 2:
                    toDeleteCount = currentSuccession - 2
                    for i in range(1, toDeleteCount + 1):
                        nums[key - i] = None
                
                currentSuccession = 1
                continue
            
            currentSuccession += 1
            
        nums[:] = [el for el in nums if el is not None]

        return len(nums)