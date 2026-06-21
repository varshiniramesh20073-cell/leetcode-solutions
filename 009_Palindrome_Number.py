class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a=x
        s=0
        while a>0:
            digit =a%10
            s=s*10+digit
            a//=10

        
        if x==s:
            return True
        else:
            return False
        
