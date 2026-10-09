class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x # store for compare 
        reverse=0 # to store the reverse number
        while x>0:
            last=x%10 # modulus get the last digit 1
            reverse=(reverse*10)+last # 0*10 +1 = 1 , 10+2=12,12*10+1=121
            x=x//10 # remove the last number 12 
        if n==reverse:
            return True  
        else: 
            return False        
