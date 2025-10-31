class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lst = nums1 + nums2
        lst.sort()
        n=len(lst)
        if n % 2 != 0:
            median=lst[n // 2]
        elif n % 2 == 0:
            median=( lst[n // 2] + lst[n // 2 - 1])/2.0
        return median
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        