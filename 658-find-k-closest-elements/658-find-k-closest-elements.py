class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        m=0
        d=abs(x-arr[0])
        for i in range(len(arr)):
            if d>abs(x-arr[i]):
                d=abs(x-arr[i])
                m=i
        l=[]
        l1=[]
        l1.append(arr[m])
        p1=m-1
        p2=m+1
        while(k>1):
            while(p1>=0 and p2<len(arr) and k>1):
                if(abs(arr[p1]-x)<=abs(arr[p2]-x)):
                    l.append(arr[p1])
                    p1-=1
                else:
                    l1.append(arr[p2])
                    p2+=1
                k-=1
            while(p1>=0 and k>1):
                l.append(arr[p1])
                p1-=1
                k-=1
            while(p2<len(arr) and k>1):
                l1.append(arr[p2])
                p2+=1
                k-=1
        l=l[::-1]
        l.extend(l1)
        return l
            
            
            
        