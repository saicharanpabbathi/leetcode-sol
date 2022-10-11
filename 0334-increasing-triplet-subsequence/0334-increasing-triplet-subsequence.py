class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l=len(nums)
        l1=[nums[0],]
        for i in range(1,l):
            if nums[i]<l1[-1]:
                l1.append(nums[i])
            else:
                l1.append(l1[-1])
        i=l-2
        m=[nums[-1],]
        while(i>=0):
            if nums[i]>m[-1]:
                m.append(nums[i])
            else:
                m.append(m[-1])
            i-=1
        m=m[::-1]
        for i in range(l):
            if l1[i]<nums[i] and nums[i]<m[i]:
                return True
        return False
        