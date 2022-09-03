def find(n,k,l,s,q):
    if n==0:
        l.append(int(s))
        return
    if int(s[q])-k>=0:
        find(n-1,k,l,s+str(int(s[q])-k),q+1)
    if int(s[q])+k<10:
        find(n-1,k,l,s+str(int(s[q])+k),q+1)
    
    
    
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        l=[]
        if k==0:
            for i in range(1,10):
                l.append(int(str(i)*n))
            return l
        for i in range(1,10):
            find(n-1,k,l,str(i),0)
        return l
        