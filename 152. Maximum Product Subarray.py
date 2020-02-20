class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxCurrent,minCurrent,result = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            nowMax = maxCurrent*nums[i]
            nowMin = minCurrent*nums[i]
            maxCurrent = max(nowMin,nowMax,nums[i])
            minCurrent = min(nowMax,nowMin,nums[i])
            result = max(maxCurrent,result)
        return result
        
        