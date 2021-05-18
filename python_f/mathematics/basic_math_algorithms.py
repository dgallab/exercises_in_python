class Level2Math():

    def factorial(self,n):
        if n==0:
            return 1
        else:
           return (n * Level2Math.factorial(self,n-1))

    def fibonacci(self,n):
        if n==1:
            return 1
        if n==0:
            return 0
        else:
            return (Level2Math.fibonacci(self,n-1) + Level2Math.fibonacci(self,n-2))

    def euclidean(self,a,b,div,gcd):
        if ((div > a) or (div > b)):
            print(gcd)
            return gcd
        while((a % div == 0) and (b % div == 0)):
            gcd=gcd*div
            a=a/div
            b=b/div
            div=2
        else:
            div=div+1
            Level2Math.euclidean(self,a,b,div,gcd)
    
    def continuedfrac(self,n,d,i):
        if (i==0):
            return n // d
        else:
            x = n // d
            y = n - x*d
            return x + 1/Level2Math.continuedfrac(self, d, y, i - 1)
    

    
       
def main():
   # print(factorial(4))
   # print(fibonacci(7))
   LM2=Level2Math()
  # print(LM2.factorial(4))
   LM2.euclidean(6683,9102,2,1)
   print(LM2.continuedfrac(17,12,3))
   
main()

