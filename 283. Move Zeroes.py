class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        count = 0
        while count < len(nums):
            if nums[count] != 0:
                nums[count],nums[index] = nums[index],nums[count]
                index += 1
            count += 1