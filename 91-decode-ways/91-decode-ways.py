class Solution:
    def numDecodings(self, s: str) -> int:
        c=1
        l=[1,]
        for i in range(len(s)):
            if (i==0 and s[i]=='0') or (i>0 and s[i]=='0' and s[i-1]=='0'):
                return 0
            elif i>0 and s[i]=='0':
                if int(s[i-1]+s[i])>26:
                    return 0
                l.append(l[c-2])
                c+=1
            elif i>0 and int(s[i-1]+s[i])<=26 and s[i-1]!='0':
                l.append(l[c-1]+l[c-2])
                c+=1
            else:
                l.append(l[c-1])
                c+=1
        return l[-1]
        