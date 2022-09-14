class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1=1
        m2=1
        ans=-11
        for i in nums:
            m3=m1
            m1=max(i,max(m2*i,m1*i))
            m2=min(i,min(m2*i,m3*i))
            ans=max(ans,m1)
        return ans
        
        