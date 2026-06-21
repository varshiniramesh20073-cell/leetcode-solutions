class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            a=x*-1
        else:
            a=x
        s=0
        while a>0:
            digit=a%10
            s=s*10+digit
            a//=10

        if s < -2**31 or s > 2**31 - 1:
            return 0
       
        if x<0:
            s= s*-1
        
        return s
        
