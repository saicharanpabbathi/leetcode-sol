class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        m=0
        nums.sort()
        i=2
        l=len(nums)
        while(i<l):
            if nums[i]<nums[i-1]+nums[i-2]:
                m=max(m,nums[i]+nums[i-1]+nums[i-2])
            i+=1
        return m
            
                
        