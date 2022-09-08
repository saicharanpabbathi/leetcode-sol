class Solution:
    def arrangeWords(self, text: str) -> str:
        if(len(text)==1):
            return text
        text=text.lower()
        l=text.split()
        a={}
        l1=[]
        for i in l:
            l2=len(i)
            if(l2 not in a):
                a[l2]=[i,]
                l1.append(l2)
            else:
                a[l2].append(i)
        l1.sort()
        s=""
        for i in l1:
            if(s==""):
                s+=" ".join(a[i])
            else:
                s+=" "+" ".join(a[i])
        return s[0].upper()+s[1:]
            
            
                
            
        
        