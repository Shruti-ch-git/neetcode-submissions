class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        o = []
        l1, l2 = 0, 0

        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] > nums2[l2]:
                o.append(nums2[l2])
                l2 += 1
            else:
                o.append(nums1[l1])
                l1 += 1

        while l1 < len(nums1):
            o.append(nums1[l1])
            l1 += 1

        while l2 < len(nums2):
            o.append(nums2[l2])
            l2 += 1

        n = len(o)
        if n % 2 == 1:
            return o[n // 2]
        else:
            return (o[n // 2] + o[n // 2 - 1]) / 2