from re import *
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=match(p,s)
        try:
            return len(m[0])==len(s)
        except:
            return False
        