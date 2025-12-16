class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            else:
                if nums1[i]<nums2[j]:
                    i+=1
                elif nums2[j]<nums1[i]:
                    j+=1
        return -1

            