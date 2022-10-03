class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        c=0
        i=0
        j=i+1
        while(j<len(colors)):
            if colors[i]!=colors[j]:
                i=j
                j=i+1
            else:
                if neededTime[i]<neededTime[j]:
                    c+=neededTime[i]
                    i=j
                    j=i+1
                else:
                    c+=neededTime[j]
                    j+=1
        return c
        