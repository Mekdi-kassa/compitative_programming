class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j=0,0
        merged=[]
        while j<n and i<m:
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i+=1
            elif nums1[i]==nums2[j]:
                merged.append(nums1[i])
                merged.append(nums2[j])
                i+=1
                j+=1
            else:
                merged.append(nums2[j])
                j+=1

        while i<m :
            merged.append(nums1[i])
            i+=1

        while j<n :
            merged.append(nums2[j])
            j+=1

        t=len(merged)
         
        nums1[:]=merged[0:t]



