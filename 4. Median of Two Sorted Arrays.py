class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine = sorted(nums1+nums2)
        length = len(combine)//2
        if len(combine)%2!=0:
            return combine[length]
        return (combine[length-1]+combine[length])/2