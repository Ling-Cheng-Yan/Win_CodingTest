class Solution:
    def Question1(self, nums, target):
        d = dict()
        for i,num in enumerate(nums):
            match = target - num
            if match in d: 
                return [d[match], i]
            else: d[num] = i