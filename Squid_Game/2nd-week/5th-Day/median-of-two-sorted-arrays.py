class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        arrlen = len(nums1)
        if (arrlen %2 == 0):
            return (nums1[int(arrlen/2)] + nums1[int((arrlen/2)-1)])/2
        else:
            return (nums1[int(arrlen/2)])