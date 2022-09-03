class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l2=[]
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<=nums2[j]):
                l2.append(nums1[i])
                i+=1
            else:
                l2.append(nums2[j])
                j+=1
        if(i<len(nums1)):
            l2.extend(nums1[i:])
        if(j<len(nums2)):
            l2.extend(nums2[j:])
        if(len(nums1)+len(nums2))&1==1:
            return l2[(len(nums1)+len(nums2))//2]
        else:
            return (l2[(len(nums1)+len(nums2))//2]+l2[(len(nums1)+len(nums2))//2-1])/2
        