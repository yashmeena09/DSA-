class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**0.5)    # c=5 the value of b is 2 

        while a<=b: # a jb tak b se small ya baraber hai tb tak loop chalega 
            total=a*a+b*b
            if total==c:
                return True 
            elif total<c: # the value of total is smaller then the target so we need incease a  
                a=a+1
            else:
                b=b-1 # here the value of taget is less and the total is high so we need to decrease the value pf b
        return False                