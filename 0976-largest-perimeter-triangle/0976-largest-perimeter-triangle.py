class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        m=0
        nums.sort()
        l=len(nums)
        i=l-1
        while(i>=2):
            if nums[i]<nums[i-1]+nums[i-2]:
                m=nums[i]+nums[i-1]+nums[i-2]
                break
            i-=1
        return m
            
                
        