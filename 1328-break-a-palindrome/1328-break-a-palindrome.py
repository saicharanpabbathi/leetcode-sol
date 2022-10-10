class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l=len(palindrome)
        if l==1:
            return ""
        elif palindrome=="a"*l:
            return "a"*(l-1)+"b"
        else:
            for i in range(l):
                if l&1==1 and i==len(palindrome)//2:
                    return palindrome[:l-1]+"b"
                if palindrome[i]!='a':
                    return palindrome[:i]+"a"+palindrome[i+1:]
        