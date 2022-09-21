class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=0
        for i in nums:
            if i&1==0:
                s+=i
        l=[]
        for i in queries:
            if nums[i[1]]&1==0 and (nums[i[1]]+i[0])&1==0:
                s+=i[0]
                nums[i[1]]+=i[0]
            elif nums[i[1]]&1==0 and (nums[i[1]]+i[0])&1==1:
                s-=nums[i[1]]
                nums[i[1]]+=i[0]
            elif (nums[i[1]]+i[0])&1==0:
                s+=nums[i[1]]+i[0]
                nums[i[1]]+=i[0]
            else:
                nums[i[1]]+=i[0]
            l.append(s)
        return l
            
        