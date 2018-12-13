class Solution:
    def singleNumber(self, nums):
        pipe = {}
        
        for num in nums:
            if not num in pipe:
                pipe[num] = True
            else:
                del pipe[num]
        
        return pipe.popitem()[0]